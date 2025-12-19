import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

        /* VIDEO DE FONDO */
        #myVideo {
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; opacity: 0.6;
        }
        .stApp { background: rgba(0, 0, 0, 0.7); }
        footer { visibility: hidden; }
        .block-container { padding-top: 1rem; padding-bottom: 5rem; }

        /* --- BOTÓN DEL MENÚ (PERSONALIZADO) --- */
        button[kind="header"] {
            z-index: 100000 !important;
            background-color: rgba(0, 20, 20, 0.9) !important; /* Fondo oscuro */
            color: #00ffff !important; /* Color neón base */
            border: 2px solid #00ffff !important; /* Borde más grueso */
            box-shadow: 0 0 10px #00ffff, inset 0 0 5px rgba(0, 255, 255, 0.5); /* Resplandor */
            border-radius: 5px !important;
            padding: 0.5rem 1rem !important; /* Más espacio */
            width: auto !important; /* Permitir que crezca para el texto */
            transition: all 0.3s ease;
            animation: neon-pulse 2s infinite alternate; /* Animación de latido */
            display: flex !important;
            align-items: center !important;
        }

        /* Efecto al pasar el mouse */
        button[kind="header"]:hover {
            background-color: #00ffff !important;
            color: #000 !important;
            box-shadow: 0 0 25px #00ffff;
        }

        /* AGREGAR TEXTO "APRETAR AQUI" AL LADO DEL ICONO */
        button[kind="header"]::after {
            content: " ► APRETAR AQUI";
            font-family: 'Orbitron', sans-serif;
            font-size: 0.8rem;
            font-weight: 700;
            margin-left: 8px;
            letter-spacing: 1px;
            white-space: nowrap; /* Evita que el texto se rompa en dos líneas */
        }

        /* Animación de pulso neón */
        @keyframes neon-pulse {
            0%   { border-color: #00ffff; color: #00ffff; box-shadow: 0 0 10px #00ffff; }
            100% { border-color: #F3F315; color: #F3F315; box-shadow: 0 0 20px #F3F315; } /* Cambia a amarillo */
        }

        /* BARRA LATERAL */
        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }

        /* SCROLLBARS */
        ::-webkit-scrollbar { width: 10px; background: #111; }
        ::-webkit-scrollbar-thumb { background: #00ffff; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #FF0055; }

        /* --- MÓVIL --- */
        @media only screen and (max-width: 768px) {
            /* Texto más corto para el botón en celulares */
            button[kind="header"]::after {
                content: " ► MENU";
            }
            .glitch-wrapper { transform: scale(0.6); margin-left: -20px; }
            .glitch { font-size: 2.5rem !important; }
            .block-container { padding-top: 4rem !important; } /* Un poco más de espacio arriba */
            #myVideo { width: 300%; left: -100%; }
        }
    </style>
    """, unsafe_allow_html=True)