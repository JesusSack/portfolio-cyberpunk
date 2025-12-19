import streamlit as st
import base64
import os

# Importamos los módulos
from styles import load_css
from header import show_header
from projects import show_projects
from sidebar import show_sidebar

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Jesus Sack | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# FUNCIÓN PARA CARGAR EL VIDEO DE FONDO 
def get_base64_video(file_name):
    try:
        with open(file_name, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# 2. CARGAR Y MOSTRAR EL VIDEO DE FONDO
video_file = get_base64_video("background.mp4")
if video_file:
    st.markdown(f"""
        <video autoplay muted loop id="myVideo">
            <source src="data:video/mp4;base64,{video_file}" type="video/mp4">
        </video>
    """, unsafe_allow_html=True)
else:
    print("⚠️ Background video not found.")

# 3. CARGAR ESTILOS CSS
load_css()

# 4. MOSTRAR LAS SECCIONES
show_sidebar()   # Barra lateral
show_header()    # Encabezado (Nombre y Terminal)
show_projects()  # Lista de proyectos