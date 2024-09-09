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
with st.expander("DIA 1 (08/10)"):
    st.write("""Sair cedo (tomar cafezin na rua rapidin) e ir apé para os seguintes destinos:""")
    st.write("""  
            - Igreja de Santo Inácio de Loyola
            - Piazza Navona
            - Pantheon (voltar mesmo pra comer o L'antico Vinaio)
            - Piazza Venezia
            - Coliseo
            """)

    st.write("""Grupo 1: Voltar do Coliseo para a praça Spagna""")
            
    st.write("""Grupo 2: Coliseo - Vaticano - Spagna""")

    st.write("""  
            - Via dei COndotti
            - Pastificio
            """)

    st.write("""Liberados""")
       
with st.expander("DIA 2 (09/10)"):
    st.write("""
            - Fontana di Trevi
            - Vaticano - Audiência Geral do Papa (07am)
            - 13:30 Museu do Vaticano/ CApela Sistina
            - Volta pro Hotel
            - Noite em Trastevere (tem onibus pra lá)
            """)

with st.expander("DIA 3 (10/10)"):
    st.write("""
        Dia mais tranquilo
                Sugestões:

                - Villa Borguese
                - Campo di Fiori com Castel San Angelo

        Saída do HOTEL 16:30
        Trem 17:30
        """)
    
st.write("Seguir para :")
st.page_link("pages/florence.py", label="Florence")