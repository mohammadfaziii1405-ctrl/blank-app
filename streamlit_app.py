import streamlit as st
import pandas as pd

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("Professional Expense Tracker")
st.divider()

amount = st.number_input("Amount", min_value=0.0, format="%.2f")
category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
date = st.date_input("Date")

if st.button("Add Expense"):
    st.success(f"Added: {category} - Rs. {amount} on {date}")
    st.balloons()

st.divider()
st.caption("Built with Streamlit | Professional Version")                                                 
                                                                                                                                               st.error("Ye symbol nahi mila! .NS laga                                                                                                                  
