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
    st.write("""Chega tarde e fica liberado - mas é bom ir no supermercado""")

with st.expander("DIA 2 (11/10)"):
    st.write("""
            - Piazza dela Republica
            - Chiesa Orsanmichelle
            - Duomo de Florença
            - Mercado Central (almoço ish)
             
            Livre
            """)

st.page_link("pages/veneza.py", label="Veneza")

with st.expander("DIA 3 (13/10)"):
    st.write("""
            - Piazza dela Signora 
            - Mercato del Porcellino
            - Ponte Vecchio
            - Piazalle Michelangelo
        
        """)
    
with st.expander("DIA 4 - TOSCANA (14/10)"):
    st.write("""
        - Greve in Chianti (passeio pela cidade)
        - Panzano in Chianti ( Almoço no Il Vescovino)
        - Siena (passeio pela cidade)
        - Panorama Crete Senesi     ( VIsta da estrada, Agriturismo Bacoleno)
        - Castiglione del Lago (Restaurante Il Pontile Experience)
        - Hotel Borgo Tre Rose Montepulciano
        """)
    
with st.expander("DIA 5 - TOSCANA (15/10)"):
    st.write("""
        - Montepulciano
        - Gladiator Shooting Spot
        - Pienza
        - Montalcino
        - volta para Florença
        """)
    
    
st.write("Seguir para :")
st.page_link("pages/paris.py", label="Paris")
