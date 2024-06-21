import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Projects", page_icon="📁", layout= "wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#---LOAD ASSETS-----
lottie_coding = load_lottieurl("https://lottie.host/c26fbd65-4e83-4516-b279-8115c39f66d5/4ZlnqwRrzx.json")




#---Sidebar-----
st.sidebar.title("Projects 📁")
st.sidebar.subheader("Information about my projects")


#----Header-----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Projects 📁")
        st.subheader("Completed Projects: ")
        st.write("wow such empty...")
        st.subheader("Projects in Progress: ")
        link_button = st.button(label="Find out more about what I'm working on!")
        if link_button:
            st.page_link("/Users/edgracia/PycharmProjects/DigitalPortfolio/pages/03_Blog.py")

    with right_column:
        st_lottie(lottie_coding, height=300, key="projects")