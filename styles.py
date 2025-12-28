import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

        /* ================================================= */
        /* BOTÓN DE MENU (MODIFICADO Y FORZADO)             */
        /* ================================================= */

        /* 1. Ocultar el icono SVG original (las 3 rayitas por defecto) */
        [data-testid="stSidebarCollapsedControl"] svg {
            display: none !important;
        }

        /* 2. Estilo de la caja del botón "MENU" */
        [data-testid="stSidebarCollapsedControl"] {
            /* Forzamos que se muestre como caja flexible */
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            
            /* Dimensiones y posición fija para que NADA lo tape */
            position: fixed !important;
            top: 15px !important;
            left: 15px !important;
            width: auto !important;
            height: auto !important;
            padding: 8px 15px !important;
            z-index: 999999 !important; /* Capa superior absoluta */
            
            /* Estética Cyberpunk */
            background-color: rgba(10, 10, 10, 0.95) !important;
            border: 2px solid #F3F315 !important; /* Amarillo Neón */
            border-radius: 4px !important;
            box-shadow: 0 0 10px rgba(243, 243, 21, 0.3);
            transition: all 0.3s ease;
        }

        /* 3. Inyectar el texto "MENU" dentro del botón */
        [data-testid="stSidebarCollapsedControl"]::after {
            content: "☰ MENU"; 
            font-family: 'Orbitron', sans-serif;
            color: #F3F315 !important;
            font-weight: 900;
            font-size: 0.9rem;
            letter-spacing: 2px;
            white-space: nowrap; /* Evita que el texto se rompa */
        }

        /* Efecto al pasar el mouse */
        [data-testid="stSidebarCollapsedControl"]:hover {
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(243, 243, 21, 0.8);
            border-color: #fff !important;
        }
        
        /* Ajuste para que el texto cambie de color en hover */
        [data-testid="stSidebarCollapsedControl"]:hover::after {
            color: #fff !important;
        }

        /* ================================================= */
        /* RESTO DE ESTILOS GENERALES                       */
        /* ================================================= */

        #myVideo {
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; opacity: 0.6;
        }

        .stApp { background: rgba(0, 0, 0, 0.7); }

        footer {visibility: hidden;}
        
        .block-container {
            padding-top: 1rem; padding-bottom: 5rem;
        }

        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }
        
        /* Botones del header general (como los 3 puntos) transparentes */
        button[kind="header"] {
            background: transparent !important;
        }

        ::-webkit-scrollbar { width: 10px; background: #111; }
        ::-webkit-scrollbar-thumb { background: #00ffff; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #FF0055; }

        /* ================================================= */
        /* MÓVIL                                            */
        /* ================================================= */

        @media only screen and (max-width: 768px) {
            
            /* Solo ajustamos posición si es necesario en móvil */
            [data-testid="stSidebarCollapsedControl"] {
                top: 10px !important;
                left: 10px !important;
            }

            .glitch-wrapper {
                transform: scale(0.65);
                margin-top: 60px; /* Espacio para que no choque con el botón MENU */
                margin-left: -10px;
            }

            .glitch { font-size: 2.5rem !important; }
            
            .block-container { padding-top: 6rem !important; }

            .cyber-card { padding: 15px; }
            
            #myVideo { width: 300%; left: -100%; }
        }
    </style>
    """, unsafe_allow_html=True)
