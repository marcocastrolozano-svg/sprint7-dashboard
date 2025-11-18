import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Proyecto Sprint 7")
st.write("Hola, Render ya está funcionando con Streamlit.")

# --- Dataset de prueba
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [1, 4, 9, 16, 25]
})

# --- Gráfico con Plotly
fig = px.scatter(df, x="x", y="y", title="Gráfico de prueba con Plotly")
st.plotly_chart(fig)

add app.py con gráfico de prueba
