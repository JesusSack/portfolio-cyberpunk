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
        footer {visibility: hidden;} /* Oculta marca de agua */
        
        /* Ajuste de márgenes generales */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 5rem;
        }

        /* 4. ARREGLO DE SUPERPOSICIÓN (Z-INDEX) */
        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }

        /* Aseguramos que el botón del menú sea visible y esté encima */
        button[kind="header"] {
            z-index: 100000 !important;
            background: transparent !important; /* Lo dejamos limpio/transparente */
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
            
            /* --- EL TEXTO "APRETE AQUÍ" ENCIMA DE TU NOMBRE --- */
            .glitch-wrapper::before {
                content: "↖ MENU: APRETE AQUÍ"; /* La flecha apunta al botón del menú */
                display: block;
                position: absolute;
                top: -30px; /* Lo subimos 30px arriba del nombre */
                left: 0;
                width: 100%;
                text-align: center; /* Centrado respecto al nombre */
                
                /* Estilo del texto */
                color: #F3F315; /* Amarillo Cyberpunk */
                font-family: 'Orbitron', sans-serif;
                font-size: 0.8rem;
                font-weight: bold;
                letter-spacing: 2px;
                text-shadow: 0 0 5px #F3F315;
                animation: blinker 2s infinite; /* Parpadeo suave */
            }

            @keyframes blinker { 
                50% { opacity: 0.3; } 
            }

            /* Ajustes de tamaño para que quepa en pantalla */
            .glitch-wrapper {
                transform: scale(0.65); /* Reducimos el nombre */
                margin-top: 20px;       /* Bajamos un poco el nombre para dar espacio al aviso */
            }

            .glitch {
                font-size: 2.5rem !important;
            }

            .block-container {
                padding-top: 4rem !important; /* Más espacio arriba para que no se pegue al borde */
            }

            .cyber-card {
                padding: 15px;
            }
            
            /* Ajuste del video en vertical */
            #myVideo {
                width: 300%;
                left: -100%;
            }
        }
    </style>
    """, unsafe_allow_html=True)