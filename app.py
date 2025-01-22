import streamlit as st

st.set_page_config(
    page_title="Streamlit Multi-Page Showcase",
    page_icon="🌟",
    layout="wide",
)

st.title("Welcome to the Streamlit Multi-Page Showcase!")
st.write(
    """
    Explore various tools by navigating to different pages using the sidebar.
    This app demonstrates:
    - Data visualization
    - Advanced map interactivity
    """
)
st.sidebar.success("Select a page to explore the tools.")
