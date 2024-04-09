import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")


with col2:
    st.title("Ardit Suice")
    content = """Hi, I'm Ikechukwu. Don't mind the picture. I'll put mine
    so many things to write but later. Just testing my skills
    """
    st.info(content)

st.write("Below you can find")