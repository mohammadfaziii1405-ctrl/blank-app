import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Price App", page_icon="📈", layout="wide")

st.title("📈 Stock Price App")
st.write("Live Stock Chart - Indian + US")

ticker = st.sidebar.text_input("Stock Symbol", "RELIANCE.NS")
period = st.sidebar.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"], index=3)

if ticker:
    try:
        data = yf.Ticker(ticker).history(period=period)
        if data.empty:
            st.error("Data nahi mila! Example: RELIANCE.NS, TCS.NS, AAPL")
        else:
            curr = data['Close'].iloc[-1]
            prev = data['Close'].iloc[-2] if len(data) > 1 else curr
            change = curr - prev
            pct = (change / prev) * 100
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Price", f"{curr:.2f}", f"{pct:.2f}%")
            c2.metric("High", f"{data['High'].max():.2f}")
            c3.metric("Low", f"{data['Low'].min():.2f}")
            
            fig = go.Figure()
            fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close']))
            fig.update_layout(title=f"{ticker} Chart", xaxis_rangeslider_visible=False, height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            st.dataframe(data.tail(10).sort_index(ascending=False))
    except Exception as e:
        st.error(f"Error: {e}")
                                                                                                            
                                                                                                                        st.write("Full Data:")
                                                                                                                                    st.dataframe(data.tail())
                                                                                                                                            else:
                                                                                                                                                        st.error("Ye symbol nahi mila! .NS lagana mat bhulo. Ex: TCS.NS")
                                                                                                                                                            except Exception as e:
                                                                                                                                                                    st.error(f"Error: {e}")
                                                                                                                                                                            st.info("Pehli baar yfinance install karna padega")
