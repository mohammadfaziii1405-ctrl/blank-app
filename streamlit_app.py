import streamlit as st
import pandas as pd

st.title("StockWise - Mera App")
st.header("GDP Comparison 2024")

data = {
    "Country": ["India (IND)", "Germany (DEU)"],
    "GDP": [3913, 4660]
}

df = pd.DataFrame(data)
st.bar_chart(df.set_index("Country"))

st.write("India GDP: $3,913 Billion")
st.write("Germany GDP: $4,660 Billion")
st.success("App ab sahi kaam karega!")import streamlit as st
import pandas as pd

st.title("StockWise - Mera App")

st.header("GDP Comparison 2024")

# Data jo aapne nikala tha
data = {
    "Country": ["India (IND)", "Germany (DEU)"],
    "GDP": [3913, 4660]
}

df = pd.DataFrame(data)
st.bar_chart(df.set_index("Country"))

st.write("🇮🇳 India GDP: $3,913 Billion")
st.write("🇩🇪 Germany GDP: $4,660 Billion")
st.success("App ab sahi kaam karega!")
                                                                                                                                               st.error("Ye symbol nahi mila! .NS laga                                                         
