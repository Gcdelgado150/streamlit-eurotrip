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

with st.expander("DIA 1 - (18/10)"):
    st.write("""
        - Chegada de tarde (15hrs)
        - Vai pro hotel e passeia la perto
        - Janta na pizza
        - volta pra casa
        """)
    
with st.expander("DIA 2 - (19/10)"):
    st.write("""
             - Acordar cedin
            - London Eye
            - Big Ben
            - Westminster Abbey
            - St. James Park
            - Buckingham Palace
            - Picadilly Circus
            - Noite em Candem Town
             """)


with st.expander("DIA 3 - (20/10)"):
    st.write("""
             - Acordar cedin
            - Sky garden
            - St. Paul's Cathedral
            - Borough Market
            - Passagem para barcelona
            """)
    
    
st.write("Seguir para :")
st.page_link("pages/barcelona.py", label="Barcelona")