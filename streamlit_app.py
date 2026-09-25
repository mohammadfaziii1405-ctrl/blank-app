import streamlit as st

st.set_page_config(page_title="Falak's App", page_icon="💖")

st.title("Hi Falak! 💖")
st.write("Ye tumhara naya app hai!")

st.divider()

name = st.text_input("Tumhara naam kya hai?")

if st.button("Click Me"):
    if name:
        st.balloons()
        st.success(f"Hello {name}! Tumhara app live ho gaya!")
    else:
        st.warning("Pehle naam toh likho Falak!")

st.info("Made with love for Falak")                                                 
                                                                                                                                               st.error("Ye symbol nahi mila! .NS laga                                                                                                                  
