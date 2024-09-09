import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_pie_gastos(df, country):
    fig = px.pie(df, values='Gastos_por_pessoa', names='Lugar', title=f'Gastos por pessoa em {country.capitalize()}')
    st.plotly_chart(fig, use_container_width=True)

def plot_pie_gastos_por_categoria(df):
    fig = px.pie(df, values='Gastos_por_pessoa', names='Tipo', title='Gastos por categoria')
    st.plotly_chart(fig, use_container_width=True)

def bar_plot_paid(df):
    fig1 = px.bar(df, x='STATUS', y='Gastos', title="Status dos gastos")

    df_grouped = df.groupby("STATUS").sum("Gastos").reset_index().sort_values(by=["Gastos"], ascending=False)
    df_grouped['formatted_gastos'] = df_grouped['Gastos'].apply(lambda x: f"R$ {x:,.2f}")

    fig1.add_trace(go.Scatter(
        x=df_grouped.STATUS, 
        y=df_grouped['Gastos'],
        text=df_grouped['formatted_gastos'],
        mode='text',
        textposition='top center',
        textfont=dict(
            size=18,
        ),
        showlegend=False
    ))
    fig1.update_yaxes(range=[0,df_grouped.Gastos.max()*1.1])
        
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

    cols = st.columns(4)
    with cols[0]:
        with st.container(border=True):
            st.markdown("<colh> Detalhes do vôo:</colh>", unsafe_allow_html=True)
            st.divider()
            df[df["Tipo"] == "Voo"][["Description", "STATUS"]]
            for i, r in df[df["Tipo"] == "Voo"][["Description", "STATUS"]].iterrows():
                c1, c2 = st.columns(2)
                with c1:
                    st.write(r['Description'])
                with c2:
                    st.write(r['STATUS'])

    with cols[1]:
        with st.container(border=True):
            st.markdown("<colh> Detalhes da estadia:</colh>", unsafe_allow_html=True)
            st.divider()
            for i, r in df[df["Tipo"] == "Estadia"][["Lugar", "STATUS"]].iterrows():
                c1, c2 = st.columns(2)
                with c1:
                    st.write(r['Lugar'])
                with c2:
                    st.write(r['STATUS'])

    with cols[2]:
        with st.container(border=True):
            st.markdown("<colh> Detalhes das atrações:</colh>", unsafe_allow_html=True)
            st.divider()
            for i, r in df[df["Tipo"] == "Atracao"][["Lugar", "STATUS"]].iterrows():
                c1, c2 = st.columns(2)
                with c1:
                    st.write(r['Lugar'])
                with c2:
                    st.write(r['STATUS'])

    with cols[3]:
        with st.container(border=True):
            st.markdown("<colh> Detalhes dos transportes:</colh>", unsafe_allow_html=True)
            st.divider()
            for i, r in df[df["Tipo"] == "Transporte"][["Lugar", "STATUS"]].iterrows():
                c1, c2 = st.columns(2)
                with c1:
                    st.write(r['Lugar'])
                with c2:
                    st.write(r['STATUS'])