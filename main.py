import streamlit as st
import styles
import sidebar
import header
import projects

# 1. Configuración
st.set_page_config(
    page_title="Jesús Sack", 
    page_icon="🦾", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Cargar Estilos y Video de Fondo
styles.load_css("background.mp4")

# 3. Componentes
sidebar.show_sidebar()
header.show_header()
projects.show_projects()