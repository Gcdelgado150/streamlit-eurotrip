import streamlit as st
import pandas as pd
from helpers import create_sidebar, plot_pie_gastos, print_status
import plotly.express as px
import os

create_sidebar()
country=os.path.splitext(os.path.basename(__file__))[0]
df = pd.read_excel("data/each_place.ods", engine="odf", sheet_name=country)
plot_pie_gastos(df, country=country)

print_status(df)


st.divider()
with st.expander("DIA 1 (12/10)"):
    st.write("""""")

