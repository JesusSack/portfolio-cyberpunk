import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

        /* VIDEO DE FONDO */
        #myVideo {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            opacity: 0.6;
        }

        /* FONDO GENERAL */
        .stApp {
            background: rgba(0, 0, 0, 0.7);
        }

        /* --- CORRECCIÓN MENÚ --- */
        /* Eliminamos header {visibility: hidden;} para que se vea el botón del menú */
        
        /* Ocultamos solo el footer (marca de agua) si quieres */
        footer {visibility: hidden;}

        /* Ajuste de márgenes superiores */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 5rem;
        }

        /* BARRA LATERAL (z-index alto para tapar contenido en móvil) */
        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }

        /* BOTÓN DE CERRAR/ABRIR SIDEBAR (Siempre visible) */
        button[kind="header"] {
            z-index: 100000 !important;
            background-color: rgba(0,0,0,0.5); /* Un fondito oscuro para que resalte */
            color: #00ffff !important; /* Color neón para la flecha */
            border: 1px solid #00ffff;
        }

        /* SCROLLBARS PERSONALIZADAS */
        ::-webkit-scrollbar {
            width: 10px;
            background: #111;
        }
        ::-webkit-scrollbar-thumb {
            background: #00ffff;
            border-radius: 5px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #FF0055;
        }

        /* --- MÓVIL (Celulares) --- */
        @media only screen and (max-width: 768px) {
            .glitch-wrapper {
                transform: scale(0.6);
                margin-left: -20px;
            }

            .glitch {
                font-size: 2.5rem !important;
            }

            .block-container {
                padding-top: 3rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }

            .cyber-card {
                padding: 15px;
            }

            .card-title {
                font-size: 1.2rem;
            }

            #myVideo {
                width: 300%;
                left: -100%;
            }
        }
    </style>
    """, unsafe_allow_html=True)