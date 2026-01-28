import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IA Smart Intelligence", layout="wide")

# --- BARRA LATERAL ---
st.sidebar.title("🤖 IA Management")
sector = st.sidebar.selectbox("Sector:", ["Hostelería", "Retail (Deportes)"])
st.sidebar.markdown("---")

# --- SECCIÓN CHATBOT SIMULADO ---
st.sidebar.subheader("Pregunta a la IA")
pregunta = st.sidebar.text_input("Ej: ¿Quién es el mejor empleado?")
if pregunta:
    if "empleado" in pregunta.lower():
        st.sidebar.success("IA: El mejor empleado hoy es **Jon (Algorta)** con un 98% de eficiencia.")
    elif "stock" in pregunta.lower():
        st.sidebar.warning("IA: Alerta, poco stock de **Cerveza** en Casco Viejo.")
    else:
        st.sidebar.info("IA: Estoy analizando los datos en tiempo real...")

# --- LÓGICA DE DATOS ---
if sector == "Hostelería":
    st.title("🍹 IA Smart Retail - Hostelería")
    df = pd.DataFrame({
        'Local': ['Las Arenas', 'Algorta', 'Puerto Viejo', 'Neguri', 'Casco Viejo'],
        'Ventas (€)': [1450, 1100, 2300, 980, 1850],
        'Stock Almacén (%)': [80, 45, 90, 20, 65],
        'Mejor Empleado': ['Miren', 'Jon', 'Ane', 'Gorka', 'Iker']
    })
    color_bar = "Local"
else:
    st.title("👟 IA Smart Retail - Sector Deportes")
    df = pd.DataFrame({
        'Local': ['Bilbao Gran Vía', 'Megapark', 'Artea', 'Durango', 'Basauri'],
        'Ventas (€)': [12000, 18500, 9500, 4200, 7800],
        'Stock Almacén (%)': [30, 75, 40, 10, 55],
        'Mejor Empleado': ['Lander', 'Nerea', 'Mikel', 'Elena', 'Peio']
    })
    color_bar = "Stock Almacén (%)"

# --- DISEÑO DE DASHBOARD ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Gráfico de Rendimiento")
    fig = px.bar(df, x='Local', y='Ventas (€)', color=color_bar, template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Estado del Almacén")
    for index, row in df.iterrows():
        nivel = row['Stock Almacén (%)']
        if nivel < 30:
            st.error(f"{row['Local']}: {nivel}% (CRÍTICO)")
        else:
            st.gauge = st.progress(nivel/100)
            st.caption(f"{row['Local']}: {nivel}%")

st.markdown("---")
st.subheader("🏆 Ranking de Empleados (Eficiencia IA)")
st.table(df[['Local', 'Mejor Empleado', 'Ventas (€)']].sort_values(by='Ventas (€)', ascending=False))
