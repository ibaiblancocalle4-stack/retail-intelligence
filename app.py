import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IA Smart Intelligence", layout="wide")

# --- SELECTOR DE SECTOR EN LA BARRA LATERAL ---
st.sidebar.title("Configuración Demo")
sector = st.sidebar.selectbox("Selecciona el Sector:", ["Hostelería (Bares/Rest.)", "Retail (Deportes/Moda)"])

if sector == "Hostelería (Bares/Rest.)":
    st.title("🍹 IA Smart Retail - Hostelería")
    locales = ['Las Arenas', 'Algorta', 'Puerto Viejo', 'Neguri', 'Casco Viejo', 'Indautxu', 'Abando', 'Getxo Centro', 'Sopela']
    datos = [1450, 1100, 2300, 980, 1850, 2100, 1600, 1250, 1400]
    label_y = "Ventas Hoy (€)"
    color_graf = "Local"
else:
    st.title("👟 IA Smart Retail - Sector Deportes")
    locales = ['Bilbao Gran Vía', 'Megapark', 'Artea', 'Durango', 'Basauri']
    datos = [12000, 18500, 9500, 4200, 7800]
    label_y = "Ventas Semanales (€)"
    color_graf = "Tienda"

df = pd.DataFrame({'Ubicación': locales, 'Rendimiento': datos})

# --- GRÁFICO ---
fig = px.bar(df, x='Ubicación', y='Rendimiento', color='Ubicación', template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

st.info(f"💡 Mostrando simulación para el sector: {sector}")
