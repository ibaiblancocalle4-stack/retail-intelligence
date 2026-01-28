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
pregunta = st.sidebar.text_input("Ej: ¿Cuál es el producto estrella?")
if pregunta:
    if "empleado" in pregunta.lower():
        st.sidebar.success("IA: El mejor empleado hoy es **Jon (Algorta)**.")
    elif "stock" in pregunta.lower():
        st.sidebar.warning("IA: Stock bajo en **Bebidas Energéticas**.")
    elif "producto" in pregunta.lower() or "seller" in pregunta.lower():
        res = "Croqueta de Jamón" if sector == "Hostelería" else "Zapatilla Running Pro"
        st.sidebar.info(f"IA: El Best Seller actual es: **{res}**")
    else:
        st.sidebar.info("IA: Analizando tendencias de mercado...")

# --- LÓGICA DE DATOS ---
if sector == "Hostelería":
    st.title("🍹 IA Smart Retail - Hostelería")
    df = pd.DataFrame({
        'Local': ['Las Arenas', 'Algorta', 'Puerto Viejo', 'Neguri', 'Casco Viejo'],
        'Ventas (€)': [1450, 1100, 2300, 980, 1850],
        'Stock Almacén (%)': [80, 45, 90, 20, 65],
        'Mejor Empleado': ['Miren', 'Jon', 'Ane', 'Gorka', 'Iker'],
        'Best Seller': ['Pintxo Tortilla', 'Croqueta Jamón', 'Raba Pelayo', 'Caña Master', 'Pintxo Txuleta']
    })
    prod_estrella = "Raba Pelayo"
    color_bar = "
