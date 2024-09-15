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

with st.expander("DIA 1 - (16/10)"):
    st.write("""
        - Chegada 09:25
        - Chegar no hotel e deixar as malas (11hrs)
        - Ir ao Trocadero 
        - Torre Eiffel
        - Hôtel des Invalides
        - Ponte Alexandre III
        - Arco do Triunfo
        - Voltar ao hotel, tomar banho
        - Voltar e Jantar vendo as luzes  da Torre Eiffel
        """)
    
with st.expander("DIA 2 - (17/10)"):
    st.write("""
            - Palacio de Versalles
            - Louvre
            - Ir para Montmartre ( Moulin Rouge e Sacre Cour)
            - Galerias Lafayete
             """)


with st.expander("DIA 3 - (18/10)"):
    st.write("""
            - Notre Dame
            - Pegar trem para Londres 
            """)