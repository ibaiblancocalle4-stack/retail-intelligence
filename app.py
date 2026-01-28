import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="IA Smart Management - Bilbao", layout="wide")

# --- BARRA LATERAL ---
st.sidebar.title("🤖 IA Management")
sector = st.sidebar.selectbox("Sector:", ["Hostelería (Bares/Rest.)", "Retail (Intersport)"])

# Chatbot avanzado con tallas e IA
st.sidebar.markdown("---")
st.sidebar.subheader("Pregunta a la IA")
pregunta = st.sidebar.text_input("Ej: ¿Qué se vende más en terraza?")
if pregunta:
    p_low = pregunta.lower()
    if "terraza" in p_low:
        st.sidebar.info("IA: En terraza dominan las **Rabas** y los **Cubalibres**.")
    elif "infantil" in p_low or "niño" in p_low:
        st.sidebar.success("IA: El stock infantil (tallas 28-35) es tu mayor flujo de caja en Basauri.")
    elif "mañana" in p_low or "venderá" in p_low:
        st.sidebar.warning("IA: Mañana hay previsión de lluvia. Impulsa la venta de paraguas y calzado impermeable.")
    else:
        st.sidebar.info("IA: Procesando datos de Bilbao y tendencias de consumo...")

# --- SECCIÓN 1: HOSTELERÍA ---
if sector == "Hostelería (Bares/Rest.)":
    st.title("🍹 IA Smart Retail - Hostelería")
    
    # 1. RENDIMIENTO DE LOS 9 LOCALES
    df_locales = pd.DataFrame({
        'Local': ['Las Arenas', 'Algorta', 'Puerto Viejo', 'Neguri', 'Casco Viejo', 'Indautxu', 'Abando', 'Deusto', 'Galdakao'],
        'Ventas (€)': [1450, 1100, 2300, 980, 1850, 2100, 1950, 1200, 850],
        'Stock (%)': [80, 45, 90, 25, 65, 70, 40, 55, 30]
    })
    
    st.subheader("📍 Rendimiento por Local (Vista General)")
    fig_loc = px.bar(df_locales, x='Local', y='Ventas (€)', color='Ventas (€)', 
                     template="plotly_dark", color_continuous_scale="Viridis")
    st.plotly_chart(fig_loc, use_container_width=True)

    st.markdown("---")
    
    # 2. DESGLOSE DETALLADO POR CATEGORÍAS
    st.subheader("🔍 Análisis Profundo: Ubicación y Categoría")
    data_h = [
        # Bebidas
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Cervezas", "Prod": "Caña", "Ventas": 450},
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Refrescos", "Prod": "Cola", "Ventas": 180},
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Infusiones", "Prod": "Té Frío", "Ventas": 90},
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Cafes", "Prod": "Café con Hielo", "Ventas": 210},
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Cubalibres", "Prod": "Gin Tonic", "Ventas": 380},
        # Comidas
        {"Ubi": "Terraza", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Rabas", "Ventas": 520},
        {"Ubi": "Terraza", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Pulpo", "Ventas": 290},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Pintxos", "Prod": "Tortilla", "Ventas": 650},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Pintxos", "Prod": "Sandwich", "Ventas": 420},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Pintxos", "Prod": "Gildas", "Ventas": 180},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Mejillones", "Ventas": 220},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Tabla Ibéricos", "Ventas": 270},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Menus", "Prod": "Menú del Día", "Ventas": 880}
    ]
    df_h = pd.DataFrame(data_h)

    # Filtros interactivos
    col1, col2, col3 = st.columns(3)
    with col1:
        ubi_sel = st.radio("Zona:", ["Terraza", "Interior"])
    with col2:
        tipo_sel = st.selectbox("Tipo:", ["Comida", "Bebida"])
    
    df_f = df_h[(df_h['Ubi'] == ubi_sel) & (df_h['Tipo'] == tipo_sel)]
    
    with col3:
        cat_sel = st.selectbox("Categoría:", df_f['Cat'].unique())

    fig_det = px.bar(df_f[df_f['Cat'] == cat_sel], x='Prod', y='Ventas', 
                     color='Ventas', template="plotly_dark", text_auto=True)
    st.plotly_chart(fig_det, use_container_width=True)

# --- SECCIÓN 2: RETAIL (INTERSPORT) ---
else:
    st.title("👟 IA Smart Retail - Intersport")
    df_r = pd.DataFrame({
        'Local': ['Bilbao Gran Vía', 'Megapark', 'Artea', 'Durango', 'Basauri'],
        'Ventas (€)': [12000, 18500, 9500, 4200, 7800],
        'Stock (%)': [35, 75, 40, 15, 55],
        'Talla Estrella': ['42.5', '39', '38', '44', '32-34 (Niño)']
    })
    
    st.subheader("📍 Ventas por Tienda y Talla Top")
    st.plotly_chart(px.bar(df_r, x='Local', y='Ventas (€)', color='Stock (%)', 
                           text='Talla Estrella', template="plotly_dark"), use_container_width=True)
    
    st.warning("⚠️ Alerta de Talla: Baja disponibilidad en tallas infantiles (32-34) en Basauri.")

# --- SECCIÓN COMÚN: EVENTOS Y WHATSAPP ---
st.markdown("---")
st.header("🏟️ IA Event Predictor - Bilbao 2026")
eventos = {
    "01/02/2026 - Derbi Athletic vs Real": "Impacto +55% en bebidas y raciones en Indautxu.",
    "08/03/2026 - Bilbao Herri Krosa": "Impacto +70% en zapatillas running e infantil.",
    "28/03/2026 - Final Four Miribilla": "Impacto +35% en hostelería zona Abando."
}
ev_sel = st.selectbox("Selecciona un evento próximo:", list(eventos.keys()))
st.success(f"🤖 Predicción IA: {eventos[ev_sel]}")

# Simulación de notificación proactiva
st.sidebar.markdown("---")
if st.sidebar.button("📲 Simular Notificación WhatsApp"):
    st.sidebar.success("Mensaje enviado: 'Aviso IA: Mañana llueve, prepara stock de paraguas y reduce terraza.'")
