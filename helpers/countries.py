import streamlit as st
import pandas as pd
from helpers import create_sidebar
import plotly.express as px

def plot_pie_gastos(df, country):
    fig = px.pie(df, values='Gastos_por_pessoa', names='Lugar', title=f'Gastos por pessoa em {country.capitalize()}')
    st.plotly_chart(fig, use_container_width=True)

def plot_pie_gastos_por_categoria(df):
    fig = px.pie(df, values='Gastos_por_pessoa', names='Tipo', title='Gastos por categoria')
    st.plotly_chart(fig, use_container_width=True)

def bar_plot_paid(df):
    fig1 = px.bar(df, x='STATUS', y='Gastos_por_pessoa', title="Status dos gastos")
    st.plotly_chart(fig1, use_container_width=True)

def total_pago_porpessoa(df):
    st.write("Total pago:")
    st.write("R$", f"{df[df['STATUS'] == 'Pago'].Gastos_por_pessoa.sum():.2f}")

def total_npago_porpessoa(df):
    st.write("Total não pago:")
    st.write("R$", f"{df[df['STATUS'] == 'não pago'].Gastos_por_pessoa.sum():.2f}")

def total_estimado(df):
    st.write("Total estimado:")
    st.write("R$", f"{df.Gastos_por_pessoa.sum():.2f}")

def print_status(df):
    st.markdown(
        """
        <style>
            colh {
                font-size: 2em
                margin: 0;
                padding: 0;
                color: yellow;
            }
        </style>""", 
        unsafe_allow_html=True
    )

    cols = st.columns(3)
    with cols[0]:
        st.markdown("<colh> Detalhes do vôo:</colh>", unsafe_allow_html=True)
        st.divider()
        for i, r in df[df["Tipo"] == "Voo"][["Description", "STATUS"]].iterrows():
            c1, c2 = st.columns(2)
            with c1:
                st.write(r['Description'])
            with c2:
                st.write(r['STATUS'])

    with cols[1]:
        st.markdown("<colh> Detalhes da estadia:</colh>", unsafe_allow_html=True)
        st.divider()
        for i, r in df[df["Tipo"] == "Estadia"][["Lugar", "STATUS"]].iterrows():
            c1, c2 = st.columns(2)
            with c1:
                st.write(r['Lugar'])
            with c2:
                st.write(r['STATUS'])

    with cols[2]:
        st.markdown("<colh> Detalhes das atrações:</colh>", unsafe_allow_html=True)
        st.divider()
        for i, r in df[df["Tipo"] == "Atracao"][["Lugar", "STATUS"]].iterrows():
            c1, c2 = st.columns(2)
            with c1:
                st.write(r['Lugar'])
            with c2:
                st.write(r['STATUS'])