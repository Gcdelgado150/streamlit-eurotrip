import streamlit as st
from datetime import datetime
import pickle
import os

def create_sidebar():
    # Clear the sidebar
    st.sidebar.title("Eurotrip")
    st.sidebar.page_link("home.py", label="Inicio") 
    st.sidebar.page_link("pages/rome.py", label="Roma")
    st.sidebar.page_link("pages/florence.py", label="Florença")
    st.sidebar.page_link("pages/venezia.py", label="Veneza")
    st.sidebar.page_link("pages/paris.py", label="Paris")
    st.sidebar.page_link("pages/london.py", label="Londres")
    st.sidebar.page_link("pages/barcelona.py", label="Barcelona")

    st.sidebar.divider()