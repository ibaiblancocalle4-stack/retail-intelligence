import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="IA Smart Intelligence", layout="wide")

# --- BARRA LATERAL ---
st.sidebar.title("🤖 IA Management")
sector = st.sidebar.selectbox("Selecciona el Sector:", ["Hostelería", "Retail (Intersport)"])
st.sidebar.markdown("---")

# --- CHATBOT SIMULADO MEJORADO ---
st.sidebar.subheader("Pregunta a la IA")
pregunta = st.sidebar.text_input("Ej: ¿Qué venderemos mañana?")

if pregunta:
    p_low = pregunta.lower()
    
    # Respuesta para Predicciones (Mañana/Futuro)
    if "mañana" in p_low or "venderá" in p_low or "predic" in p_low:
        if sector == "Hostelería":
            st.sidebar.info("IA: Mañana es jueves en Bilbao. Preveo un aumento del 15% en **Pintxos de Tortilla** debido al 'Afterwork'.")
        else:
            st.sidebar.info("IA: Previsión para mañana: Se venderán unas **15-20 Botas de Monte** en Durango debido al aviso de nieve en el Anboto.")
    
    # Respuesta para Best Sellers y Botas
    elif "estrella" in p_low or "seller" in p_low or "vende" in p_low or "botas" in p_low:
        res = "Croqueta de Jamón" if sector == "Hostelería" else "Zapatilla Running Pro y Botas de Monte"
        st.sidebar.info(f"IA: El producto top ahora mismo es: **{res}**")
    
    # Respuesta para Empleados
    elif "empleado" in p_low or "quién" in p_low:
        st.sidebar.success("IA: El mejor empleado hoy es **Jon** (Hostelería) o **Nerea** (Retail).")
    
    else:
        st.sidebar.info("IA: Estoy procesando tu consulta con los datos históricos del grupo...")

# --- LÓGICA DE DATOS ---
if sector == "Hostelería":
    st.title("🍹 IA Smart Retail - Hostelería")
    df = pd.DataFrame({
        'Local': ['Las Arenas', 'Algorta', 'Puerto Viejo', 'Neguri', 'Casco Viejo'],
        'Ventas (€)': [1450, 1100, 2300, 980, 1850],
        'Stock (%)': [80, 45, 90, 25, 65],
        'Mejor Empleado': ['Miren', 'Jon', 'Ane', 'Gorka', 'Iker'],
        'Best Seller': ['Pintxo Tortilla', 'Croqueta Jamón', 'Raba Pelayo', 'Caña Master', 'Pintxo Txuleta']
    })
    prod_estrella = "Raba Pelayo"
    color_bar = "Local"
else:
    st.title("👟 IA Smart Retail - Sector Deportes")
    df = pd.DataFrame({
        'Local': ['Bilbao Gran Vía', 'Megapark', 'Artea', 'Durango', 'Basauri'],
        'Ventas (€)': [12000, 18500, 9500, 4200, 7800],
        'Stock (%)': [35, 75, 40, 15, 55],
        'Mejor Empleado': ['Lander', 'Nerea', 'Mikel', 'Elena', 'Peio'],
        'Best Seller': ['Camiseta Athletic', 'Zapatilla Running', 'Sudadera Training', 'Botas Monte', 'Pala Pádel']
    })
    prod_estrella = "Zapatilla Running"
    color_bar = "Stock (%)"

# --- MÉTRICAS SUPERIORES ---
m1, m2, m3 = st.columns(3)
m1.metric("Ventas Totales Grupo", f"{df['Ventas (€)'].sum()} €", "+12%")
m2.metric("Producto Best Seller", prod_estrella)
m3.metric("Eficiencia de Inventario", f"{int(df['Stock (%)'].mean())}%", "-2%")

st.markdown("---")

# --- DASHBOARD ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Rendimiento por Local y Producto Estrella")
    # El gráfico ahora muestra el Best Seller sobre cada barra
    fig = px.bar(df, x='Local', y='Ventas (€)', color=color_bar, text='Best Seller', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📦 Niveles de Almacén")
    for i, row in df.iterrows():
        nivel = row['Stock (%)']
        if nivel < 30:
            st.error(f"{row['Local']}: {nivel}% (CRÍTICO)")
        else:
            st.progress(nivel/100)
            st.caption(f"{row['Local']}: {nivel}%")

st.subheader("🏆 Resumen Ejecutivo")
st.table(df[['Local', 'Best Seller', 'Mejor Empleado', 'Ventas (€)']])
