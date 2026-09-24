import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock Price App", page_icon="📈")

st.title("📈 Stock Price App")
st.write("Koi bhi company ka live stock dekho!")

# Stock ka naam
ticker = st.text_input("Stock Symbol likho (jaise: TCS.NS, RELIANCE.NS, INFY.NS)", "TCS.NS")

if ticker:
    try:
            stock = yf.Ticker(ticker)
                    data = stock.history(period="1mo")
                            
                                    if not data.empty:
                                                st.subheader(f"{ticker} ka last 1 mahine ka chart")
                                                            st.line_chart(data['Close'])
                                                                        
                                                                                    current_price = data['Close'][-1]
                                                                                                st.metric(label="Current Price", value=f"Rs. {current_price:.2f}")
                                                                                                            
                                                                                                                        st.write("Full Data:")
                                                                                                                                    st.dataframe(data.tail())
                                                                                                                                            else:
                                                                                                                                                        st.error("Ye symbol nahi mila! .NS lagana mat bhulo. Ex: TCS.NS")
                                                                                                                                                            except Exception as e:
                                                                                                                                                                    st.error(f"Error: {e}")
                                                                                                                                                                            st.info("Pehli baar yfinance install karna padega")
