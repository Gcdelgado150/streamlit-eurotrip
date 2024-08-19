import streamlit as st
from helpers import create_sidebar, plot_pie_gastos_por_categoria, bar_plot_paid, total_pago_porpessoa, total_npago_porpessoa, total_estimado
import pandas as pd
import plotly.express as px
import datetime
from datetime import datetime

def transform_hour(ser):
    if ser >= 10:
        return f"{int(ser)}"
    else:
        return f"0{int(ser)}"
    
st.set_page_config(layout="wide")

create_sidebar()

df = pd.read_csv("data/roteiro.csv")
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

# Edit arrival times
df.loc[df["Destination"] == "Madrid", ["Start_Date"]] = f"2024-10-07 {transform_hour(df.loc[df['Destination'] == 'Madrid', ['Chegada']].values[0])}:00:00"
df.loc[df["Destination"] == "Madrid", ["End_Date"]] = f"2024-10-07 {transform_hour(df.loc[df['Destination'] == 'Madrid', ['Saida']].values[0])}:00:00"
df.loc[df["Destination"] == "Roma", ["Start_Date"]] = f"2024-10-07 {transform_hour(df.loc[df['Destination'] == 'Roma', ['Chegada']].values[0])}:35:00"

date = datetime.now()
order_country = df.Destination.tolist()

days_left = (df.loc[0, "Start_Date"] - date).days
if days_left >= 0:
    st.markdown(f"<p style='font-size: 24px; color: white; font-weight: bold;'>Faltam <span style='color: red;'>{days_left}</span> dias para a viagem.</p>", unsafe_allow_html=True)


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

import os
all_dfs = []
for page in os.listdir("pages"):
    df = pd.read_excel("data/each_place.ods", engine="odf", sheet_name=page.split(".")[0])
    all_dfs.append(df)

all_dfs = pd.concat(all_dfs)
plot_pie_gastos_por_categoria(all_dfs)
col_pago, col_npago = st.columns(2)
with col_pago:
    total_pago_porpessoa(all_dfs)
with col_npago:
    total_npago_porpessoa(all_dfs)
total_estimado(all_dfs)
bar_plot_paid(all_dfs)

    # st.write()