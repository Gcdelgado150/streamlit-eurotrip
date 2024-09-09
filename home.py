import streamlit as st
from helpers import create_sidebar, plot_pie_gastos_por_categoria, bar_plot_paid, total_pago_porpessoa, total_npago_porpessoa, total_estimado
import pandas as pd
import plotly.express as px
import datetime
from datetime import datetime
import os

    
st.set_page_config(layout="wide")
create_sidebar()

df = pd.read_csv("data/roteiro.csv")
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

date = datetime.now()
days_left = (df.loc[0, "Start_Date"] - date).days
if days_left >= 0:
    st.markdown(f"<p style='font-size: 24px; color: white; font-weight: bold;'>Faltam <span style='color: red;'>{days_left}</span> dias para a viagem.</p>", unsafe_allow_html=True)

order_country = df.Destination.tolist()

for i, row in df.iterrows():    
    # Combine Start_Date and Chegada
    new_start_date = f"{row['Start_Date']} {row['Chegada']}"
    new_end_date = f"{row['End_Date']} {row['Saida']}"
    
    # Update the DataFrame for the current row
    df.loc[i, 'Start_Date'] = new_start_date
    df.loc[i, "End_Date"] = new_end_date

# Interactive Timeline Visualization
if not df.empty:
    fig = px.timeline(df, 
                        x_start="Start_Date", 
                        x_end="End_Date", 
                        y="Destination", 
                        color="Destination",
                        title="Cronograma", 
                        labels={'Destination': 'Destino',
                                'Start_Date' : 'Chegada',
                                'End_Date' : 'Saída'})
    fig.update_yaxes(categoryorder="array", categoryarray=order_country)
    fig.add_vline(x=date, line_width=3, line_color="black")
    st.plotly_chart(fig)
st.divider()
all_dfs = []
for page in os.listdir("pages"):
    df = pd.read_excel("data/each_place.ods", engine="odf", sheet_name=page.split(".")[0])
    all_dfs.append(df)

all_dfs = pd.concat(all_dfs)
plot_pie_gastos_por_categoria(all_dfs)
st.divider()

col_pago, col_npago, col_estimado = st.columns(3)
with col_pago:
    with st.container(border=True):
        total_pago_porpessoa(all_dfs)
with col_npago:
    with st.container(border=True):
        total_npago_porpessoa(all_dfs)
with col_estimado:
    with st.container(border=True):
        total_estimado(all_dfs)

st.divider()
bar_plot_paid(all_dfs)