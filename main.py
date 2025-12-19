import streamlit as st
import base64
import os

#  IMPORTACIONES 
from styles import load_css
from header import show_header
from projects import show_projects
from sidebar import show_sidebar
from agent import show_chatbot

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Jesus Sack | AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

#  FUNCIÓN VIDEO FONDO
def get_base64_video(file_name):
    try:
        with open(file_name, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# 2. CARGAR VIDEO
video_file = get_base64_video("background.mp4")
if video_file:
    st.markdown(f"""
        <video autoplay muted loop id="myVideo">
            <source src="data:video/mp4;base64,{video_file}" type="video/mp4">
        </video>
    """, unsafe_allow_html=True)

# 3. CARGAR ESTILOS
load_css()

# 4. ESTRUCTURA DE LA PÁGINA
show_sidebar()
show_header()
# Tabs para separar el contenido visual del Chatbot
tab1, tab2 = st.tabs(["🚀 PROJECTS & WORK", "🧠 AI AGENT (CHAT)"])

with tab1:
    show_projects()

with tab2:
    show_chatbot()