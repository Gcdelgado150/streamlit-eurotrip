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


st.write("Roteiro")

st.write("""DIA 1
Chegar no hotel e deixar as malas
Ir ao Trocadero e no Campo de Marte para ver Torre Eiffel
Almoçar perto da Ponte Alexandre III
Voltar ao hotel, tomar banho
Ir para Montmartre ( Moulin Rouge e Sacre Cour)
Voltar e ver as luzes da Torre Eiffel
Jantar vendo as luzes 

DIA 2
Palacio de Versalles
Louvre
Notre Dame


DIA 3
Galerias Lafayete
Arco do Triunfo
Pegar trem para Londres 
""")