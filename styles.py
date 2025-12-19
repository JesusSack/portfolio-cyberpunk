import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

        /* 1. VIDEO DE FONDO */
        #myVideo {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            opacity: 0.6;
        }

        /* 2. FONDO GENERAL */
        .stApp {
            background: rgba(0, 0, 0, 0.7);
        }

        /* 3. LIMPIEZA DE INTERFAZ */
        footer {visibility: hidden;}
        
        .block-container {
            padding-top: 1rem;
            padding-bottom: 5rem;
        }

        /* 4. ARREGLO DE SUPERPOSICIÓN (Z-INDEX) */
        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }

        button[kind="header"] {
            z-index: 100000 !important;
            background: transparent !important;
            color: #00ffff !important;
        }

        /* 5. SCROLLBARS PERSONALIZADAS */
        ::-webkit-scrollbar { width: 10px; background: #111; }
        ::-webkit-scrollbar-thumb { background: #00ffff; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #FF0055; }

        /* ================================================= */
        /* 6. OPTIMIZACIÓN MÓVIL (SOLO CELULARES) */
        /* ================================================= */
        @media only screen and (max-width: 768px) {
            
            /* --- TEXTO "PRESIONE AQUÍ" MODIFICADO --- */
            .glitch-wrapper::before {
                content: "↖ MENU: PRESIONE AQUÍ";
                display: block;
                position: absolute;
                top: -40px; /* Un poco más arriba por el tamaño */
                left: 0;
                width: 100%;
                text-align: left; /* Alineado a la izquierda */
                padding-left: 10px; /* Pequeño margen desde el borde */
                
                /* Estilo del texto */
                color: #F3F315;
                font-family: 'Orbitron', sans-serif;
                font-size: 1.1rem; /* Más grande (antes 0.8rem) */
                font-weight: bold;
                letter-spacing: 1px;
                text-shadow: 0 0 5px #F3F315;
                animation: blinker 2s infinite;
            }

            @keyframes blinker { 
                50% { opacity: 0.3; } 
            }

            /* Ajustes de tamaño y posición del nombre */
            .glitch-wrapper {
                transform: scale(0.65);
                margin-top: 25px; /* Más espacio arriba */
                margin-left: -10px; /* Ajuste leve a la izquierda */
            }

            .glitch {
                font-size: 2.5rem !important;
            }

            .block-container {
                padding-top: 4.5rem !important; /* Más aire arriba */
            }

            .cyber-card {
                padding: 15px;
            }
            
            #myVideo {
                width: 300%;
                left: -100%;
            }
        }
    </style>
    """, unsafe_allow_html=True)