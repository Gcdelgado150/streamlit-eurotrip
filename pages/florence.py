import streamlit as st
import pandas as pd
from helpers import create_sidebar, plot_pie_gastos, print_status
import plotly.express as px
import os


st.set_page_config(layout="wide")
create_sidebar()

country=os.path.splitext(os.path.basename(__file__))[0]
df = pd.read_excel("data/each_place.ods", engine="odf", sheet_name=country)
plot_pie_gastos(df, country=country)
print_status(df)


st.divider()
with st.expander("DIA 1 (10/10)"):
    st.write("""Chega tarde e fica liberado""")

with st.expander("DIA 2 (11/10)"):
    st.write("""
             - Piazza dela Republica
             - Chiesa Orsanmichelle
            - Duomo de Florença
            - Mercado Central (almoço ish)
             
            Livre
            """)

st.page_link("pages/venezia.py", label="Venezia")

with st.expander("DIA 3 (13/10)"):
    st.write("""
             - Piazza dela Signora 
             - Mercato del Porcellino
            - Ponte Vecchio
            - Piazalle Michelangelo
        
        """)
    
with st.expander("DIA 4 - TOSCANA (14/10)"):
    st.write("""
        
        """)
    
st.write("Seguir para :")
st.page_link("pages/paris.py", label="Paris")
