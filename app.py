import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="IA Smart Management - Bilbao", layout="wide")

# --- BARRA LATERAL: IA Y CHATBOT ---
st.sidebar.title("🤖 IA Management")
sector = st.sidebar.selectbox("Sector:", ["Hostelería (Bares/Rest.)", "Retail (Intersport)"])

st.sidebar.markdown("---")
st.sidebar.subheader("Pregunta a la IA")
pregunta = st.sidebar.text_input("Ej: ¿Qué se vende más en terraza?")

# Lógica del Chatbot (Respuestas dinámicas)
if pregunta:
    p_low = pregunta.lower()
    if "terraza" in p_low:
        st.sidebar.info("IA: En terraza el producto líder son las **Rabas** y los **Cubalibres**.")
    elif "infantil" in p_low or "niño" in p_low:
        st.sidebar.success("IA: En Retail, las tallas **28-35** de Adidas Tensaur son el Top Ventas.")
    elif "mañana" in p_low or "venderá" in p_low:
        st.sidebar.warning("IA: Mañana hay previsión de **lluvia**. El stock de paraguas debe estar en primera línea.")
    else:
        st.sidebar.info("IA: Analizando tendencias en Bilbao para darte la mejor respuesta...")

# --- SECCIÓN 1: HOSTELERÍA DETALLADA ---
if sector == "Hostelería (Bares/Rest.)":
    st.title("🍹 Panel de Control: Hostelería Inteligente")
    
    # Base de datos jerárquica
    data_h = [
        # TERRAZA
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Cervezas", "Prod": "Caña Master", "Ventas": 450},
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Refrescos", "Prod": "Cola-Zero", "Ventas": 210},
        {"Ubi": "Terraza", "Tipo": "Bebida", "Cat": "Cubalibres", "Prod": "Gin Tonic Premium", "Ventas": 380},
        {"Ubi": "Terraza", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Rabas Pelayo", "Ventas": 520},
        {"Ubi": "Terraza", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Pulpo a la Gallega", "Ventas": 290},
        # INTERIOR
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Pintxos", "Prod": "Tortilla de Patata", "Ventas": 650},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Pintxos", "Prod": "Sandwich Mixto", "Ventas": 410},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Pintxos", "Prod": "Gildas", "Ventas": 180},
        {"Ubi": "Interior", "Tipo": "Bebida", "Cat": "Cafes", "Prod": "Café Solo", "Ventas": 320},
        {"Ubi": "Interior", "Tipo": "Bebida", "Cat": "Infusiones", "Prod": "Té Rojo", "Ventas": 95},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Menus", "Prod": "Menú Ejecutivo", "Ventas": 880},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Mejillones", "Ventas": 220},
        {"Ubi": "Interior", "Tipo": "Comida", "Cat": "Raciones", "Prod": "Tabla Ibéricos", "Ventas": 270}
    ]
    df_h = pd.DataFrame(data_h)

    st.subheader("📊 Análisis de Ventas por Ubicación")
    col1, col2, col3 = st.columns(3)
    with col1:
        ubi_sel = st.radio("Selecciona Zona:", ["Terraza", "Interior"])
    with col2:
        tipo_sel = st.selectbox("Tipo de Consumo:", ["Comida", "Bebida"])
    
    df_f = df_h[(df_h['Ubi'] == ubi_sel) & (df_h['Tipo'] == tipo_sel)]
    
    with col3:
        cat_sel = st.selectbox("Categoría Específica:", df_f['Cat'].unique())

    # Gráfico Detallado
    df_final = df_f[df_f['Cat'] == cat_sel]
    fig_h = px.bar(df_final, x='Prod', y='Ventas', color='Ventas', 
                 title=f"Ventas en {ubi_sel}: {cat_sel}", template="plotly_dark", text_auto=True)
    st.plotly_chart(fig_h, use_container_width=True)

# --- SECCIÓN 2: RETAIL (INTERSPORT) ---
else:
    st.title("👟 Panel de Control: Intersport Intelligence")
    
    col_r1, col_r2 = st.columns([2, 1])
    
    with col_r1:
        st.subheader("Análisis de Tallas y Modelos")
        df_r = pd.DataFrame({
            'Categoría': ['Running Hombre', 'Running Mujer', 'Infantil', 'Montaña'],
            'Modelo Top': ['Nike Pegasus 40', 'Asics Novablast', 'Adidas Tensaur', 'Salomon X Ultra'],
            'Talla Más Vendida': ['42.5', '38', '32-34', '43'],
            'Ventas (€)': [12500, 9800, 15600, 7400]
        })
        fig_r = px.bar(df_r, x='Categoría', y='Ventas (€)', color='Categoría', text='Modelo Top', template="plotly_dark")
        st.plotly_chart(fig_r, use_container_width=True)
    
    with col_r2:
        st.subheader("📦 Stock Crítico")
        st.error("Durango: Botas Monte (15%)")
        st.warning("Megapark: Running Infantil (28%)")
        st.progress(0.15)
        st.progress(0.28)

# --- SECCIÓN 3: EVENTOS Y WHATSAPP (COMÚN) ---
st.markdown("---")
st.header("🏟️ IA Event Predictor - Bilbao")

eventos = {
    "01/02/2026 - Athletic vs Real Sociedad": "Impacto +55%. Refuerzo de bebidas y camisetas en zona Indautxu.",
    "08/03/2026 - Bilbao Herri Krosa": "Impacto +70%. Stock masivo necesario en categoría INFANTIL.",
    "28/03/2026 - Concierto en el BEC": "Impacto +30%. Aumento de menús rápidos y calzado cómodo."
}
ev_sel = st.selectbox("Próximo evento detectado:", list(eventos.keys()))
st.success(f"🤖 **Predicción IA:** {eventos[ev_sel]}")

# Simulación de WhatsApp
st.sidebar.markdown("---")
if st.sidebar.button("📲 Simular WhatsApp al Cliente"):
    st.sidebar.success("Enviado: 'Aviso IA: Mañana llueve. Prepara paraguas y reduce stock de terraza.'")

# Comparativa final
with st.expander("¿Por qué esta IA es mejor que un Excel?"):
    st.write("- **Proactiva**: Te avisa por WhatsApp antes de que pase.")
    st.write("- **Contextual**: Sabe si hay fútbol en San Mamés o si llueve.")
    st.write("- **Precisa**: Te da la talla exacta (32-34 infantil) que debes pedir.")
