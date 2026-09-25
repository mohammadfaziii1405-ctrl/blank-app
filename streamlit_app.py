import streamlit as st

st.title("Expense Tracker - Kotpura")
st.divider()
st.success("Kotpura App is Working!")

amount = st.number_input("Amount", min_value=1)
category = st.selectbox("Category", 
    ["Food", "Travel", "Shopping", "Bills", "Kotpura"])
place = st.text_input("Place", "Kotpura")

if st.button("Add Expense"):
    st.write("Added:", amount, category, place)
    st.balloons()

st.caption("Built for Kotpura")
                                                                                                                                               st.error("Ye symbol nahi mila! .NS laga                                                         
