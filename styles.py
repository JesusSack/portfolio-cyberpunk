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

        /* Ocultamos el footer de Streamlit */
        footer {visibility: hidden;}

        /* Ajuste de márgenes */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 5rem;
        }

        /* BARRA LATERAL (Siempre encima en móvil) */
        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }

        /* BOTÓN DE MENÚ (Configuración Base) */
        button[kind="header"] {
            z-index: 100000 !important;
            /* Le damos un fondo suave para que se vea sobre el video */
            background-color: rgba(0,0,0,0.3) !important;
            color: #00ffff !important;
            border: 1px solid rgba(0, 255, 255, 0.3) !important;
        }

        /* SCROLLBARS */
        ::-webkit-scrollbar { width: 10px; background: #111; }
        ::-webkit-scrollbar-thumb { background: #00ffff; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #FF0055; }

        /* --- CONFIGURACIÓN SOLO PARA CELULARES --- */
        @media only screen and (max-width: 768px) {
            
            /* 1. AGREGAR TEXTO "APRETE AQUÍ" AL LADO DEL BOTÓN */
            button[kind="header"]::after {
                content: " ⬅ APRETE AQUÍ";
                color: #F3F315; /* Amarillo Cyberpunk */
                font-family: 'Orbitron', sans-serif;
                font-size: 0.7rem;
                font-weight: bold;
                margin-left: 8px;
                text-shadow: 0 0 5px #F3F315;
                animation: blinker 1.5s linear infinite; /* Parpadeo suave */
                vertical-align: middle;
            }

            @keyframes blinker { 
                50% { opacity: 0.3; } 
            }

            /* 2. Ajustes de tamaño para el título Glitch */
            .glitch-wrapper {
                transform: scale(0.6);
                margin-left: -20px;
            }

            .glitch {
                font-size: 2.5rem !important;
            }

            /* 3. Ajustes de espaciado */
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