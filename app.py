import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="IA Smart Intelligence", layout="wide")

# --- BARRA LATERAL (CONFIGURACIÓN) ---
st.sidebar.title("🤖 IA Management")
sector = st.sidebar.selectbox("Selecciona el Sector:", ["Hostelería (Bares/Rest.)", "Retail (Intersport)"])
st.sidebar.markdown("---")

# --- CHATBOT AVANZADO ---
st.sidebar.subheader("Pregunta a la IA")
pregunta = st.sidebar.text_input("Ej: ¿Qué venderemos mañana?")

if pregunta:
    p_low = pregunta.lower()
    
    # 1. Predicciones (Mañana/Futuro/Eventos)
    if any(x in p_low for x in ["mañana", "venderá", "prediccion", "evento"]):
        if sector == "Hostelería (Bares/Rest.)":
            st.sidebar.info("IA: Mañana es jueves en Bilbao. Preveo un aumento del 15% en Pintxos de Tortilla por el Afterwork.")
        else:
            st.sidebar.info("IA: Previsión: Se venderán 15-20 Botas de Monte en Durango debido al aviso de nieve en el Anboto.")
            
    # 2. Tallas y Categoría Infantil (Solo Retail)
    elif any(x in p_low for x in ["talla", "infantil", "niño", "bebe"]):
        if sector == "Retail (Intersport)":
            st.sidebar.success("""
            **Análisis de Tallas IA:**
            * **Infantil:** Éxito en tallas **28-35**.
            * **Adulto:** Talla más vendida **42.5**.
            * *Tip:* Reponer stock infantil antes de marzo (Herri Krosa).
            """)
        else:
            st.sidebar.warning("IA: Esa consulta es específica de Retail.")

    # 3. Productos y Marcas
    elif any(x in p_low for x in ["producto", "marca", "zapatilla", "estrella", "seller", "botas"]):
        if sector == "Retail (Intersport)":
            st.sidebar.info("IA: Top Ventas: **Nike Pegasus 40** (Running) y **Adidas Tensaur** (Infantil).")
        else:
            st.sidebar.info("IA: El producto estrella hoy es: **Raba Pelayo**.")
            
    # 4. Empleados
    elif "empleado" in p_low or "quien" in p_low:
        st.sidebar.success("IA: El mejor empleado hoy es **Jon (Algorta)** o **Nerea (Bilbao)**.")
    else:
        st.sidebar.info("IA: Analizando datos históricos y tendencias de Bilbao...")

# --- LÓGICA DE DATOS SEGÚN SECTOR ---
if sector == "Hostelería (Bares/Rest.)":
    st.title("🍹 IA Smart Retail - Hostelería")
    df = pd.DataFrame({
        'Local': ['Las Arenas', 'Algorta', 'Puerto Viejo', 'Neguri', 'Casco Viejo'],
        'Ventas (€)': [1450, 1100, 2300, 980, 1850],
        'Stock (%)': [80, 45, 90, 25, 65],
        'Mejor Empleado': ['Miren', 'Jon', 'Ane', 'Gorka', 'Iker'],
        'Best Seller': ['Pintxo Tortilla', 'Croqueta Jamón', 'Raba Pelayo', 'Caña Master', 'Pintxo Txuleta']
    })
    color_bar = "Local"
else:
    st.title("👟 IA Smart Retail - Sector Deportes")
    df = pd.DataFrame({
        'Local': ['Bilbao Gran Vía', 'Megapark', 'Artea', 'Durango', 'Basauri'],
        'Ventas (€)': [12000, 18500, 9500, 4200, 7800],
        'Stock (%)': [35, 75, 40, 15, 55],
        'Mejor Empleado': ['Lander', 'Nerea', 'Mikel', 'Elena', 'Peio'],
        'Best Seller': ['Nike Pegasus', 'Zapatilla Running', 'Sudadera Training', 'Botas Monte', 'Pala Pádel']
    })
    color_bar = "Stock (%)"

# --- MÉTRICAS SUPERIORES ---
m1, m2, m3 = st.columns(3)
m1.metric("Venta Total Grupo", f"{df['Ventas (€)'].sum()} €", "+12%")
m2.metric("Estado Almacén", "Optimizado" if df['Stock (%)'].mean() > 50 else "Revisar Stock", "-2%")
m3.metric("Eficiencia Media", "88%", "+5%")

st.markdown("---")

# --- DASHBOARD PRINCIPAL ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Rendimiento y Productos Estrella")
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

# --- PREDICCIÓN POR EVENTOS BILBAO ---
st.markdown("---")
st.header("🏟️ IA Event Predictor - Bilbao")

eventos_bilbao = {
    "01/02/2026 - Athletic vs Real Sociedad (Derbi)": {"impacto": 0.55, "desc": "Máximo impacto en Indautxu y Centro. Reforzar bebidas/textil."},
    "08/03/2026 - Bilbao Herri Krosa": {"impacto": 0.70, "desc": "Pico masivo en calzado infantil y running adulto."},
    "28/03/2026 - Final Four Basketball (Miribilla)": {"impacto": 0.35, "desc": "Aumento de afluencia en locales cercanos al Arena."}
}

evento_sel = st.selectbox("Próximos eventos en Bilbao:", list(eventos_bilbao.keys()))
st.info(f"🤖 **Análisis de la IA:** {eventos_bilbao[evento_sel]['desc']}")

# --- WHATSAPP SIMULADO ---
st.sidebar.markdown("---")
st.sidebar.subheader("📲 Notificaciones WhatsApp")
if st.sidebar.button("Simular Alerta a Cliente"):
    msg = "🌧️ *AVISO IA*: Mañana llueve en Bilbao. Recomendamos ajustar stock de productos frescos y destacar paraguas/botas."
    st.sidebar.success(f"Enviado al móvil del cliente: {msg}")

# --- TABLA COMPARATIVA ---
with st.expander("Ver Comparativa vs Sistemas Tradicionales"):
    st.markdown("""
    | Ventaja | Gestión Tradicional | **Nuestra IA Smart** |
    | :--- | :--- | :--- |
    | **Alertas** | Tienes que buscar el dato | **WhatsApp Proactivo** |
    | **Clima** | No lo integra | **Cruza datos con AEMET** |
    | **Eventos** | Intuición del dueño | **Predicción por calendario** |
    """)

st.table(df[['Local', 'Best Seller', 'Mejor Empleado', 'Ventas (€)']])
