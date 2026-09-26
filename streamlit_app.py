import streamlit as st
import pandas as pd

st.set_page_config(page_title="StockWise", page_icon="📈", layout="centered")

# --- Custom Theme ---
st.markdown("""
<style>
    .stApp { background-color: #f5f7ff; }
    h1 { color: #4a00e0; }
</style>
""", unsafe_allow_html=True)

st.title("StockWise - SMART. SIMPLE. INFORMED. 📈")
st.header("Welcome to StockWise!")

# Sample Stock Data
data = {
    "Company": ["TCS", "Reliance", "Infosys"],
    "Price": [3500, 2800, 1500]
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Company"))

st.success("StockWise App ab sahi kaam karega!")

# --- About App & Owner (Safe Version) ---
st.divider()
with st.expander("ℹ️ About StockWise App"):
    st.markdown("**StockWise - SMART. SIMPLE. INFORMED.** This app provides stock information for educational purposes.")
    st.markdown("---")
    st.markdown("#### 👩‍💼 About The Owner")
    st.markdown("""
    **Owner:** Ashmira Falak  
    **From:** Maharashtra, India  
    
    I am the founder of StockWise. My mission is to make the stock market simple, 
    smart and easy to understand for every beginner in India.
    """)        
