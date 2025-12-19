import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

        /* 1. VIDEO DE FONDO */
        #myVideo {
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; opacity: 0.6;
        }

        /* 2. FONDO GENERAL */
        .stApp { background: rgba(0, 0, 0, 0.7); }

        /* 3. LIMPIEZA */
        footer {visibility: hidden;}
        
        .block-container {
            padding-top: 1rem; padding-bottom: 5rem;
        }

        /* 4. SIDEBAR & MENU BUTTON */
        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }

        button[kind="header"] {
            z-index: 100000 !important;
            background: transparent !important;
            color: #00ffff !important;
        }

        /* 5. SCROLLBARS */
        ::-webkit-scrollbar { width: 10px; background: #111; }
        ::-webkit-scrollbar-thumb { background: #00ffff; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #FF0055; }

        /* ================================================= */
        /* 6. OPTIMIZACIÓN MÓVIL (AJUSTE DE ALTURA) */
        /* ================================================= */
        @media only screen and (max-width: 768px) {
            
            /* FLECHA Y TEXTO */
            .glitch-wrapper::before {
                content: "↖--------- MENU: PRESIONE AQUÍ"; 
                display: block;
                position: absolute;
                
                /* AJUSTE DE ALTURA: -90px lo sube "2 espacios" más respecto al anterior */
                top: -90px;       
                left: -40px;
                width: 120%;
                text-align: left;
                
                color: #F3F315;
                font-family: 'Orbitron', sans-serif;
                font-size: 1.3rem;
                font-weight: 900;
                letter-spacing: 1px;
                text-shadow: 0 0 10px #F3F315;
                
                animation: blinker 1.5s infinite alternate;
            }

            @keyframes blinker { 
                0% { opacity: 0.4; text-shadow: 0 0 5px #F3F315; }
                100% { opacity: 1; text-shadow: 0 0 20px #F3F315, 0 0 10px #FF0055; }
            }

            /* Separamos más el nombre hacia abajo para que no se choque con la flecha */
            .glitch-wrapper {
                transform: scale(0.65);
                margin-top: 60px; /* Más margen superior */
                margin-left: -15px;
            }

            .glitch { font-size: 2.5rem !important; }
            
            /* Damos más aire al contenedor general */
            .block-container { padding-top: 6rem !important; }

            .cyber-card { padding: 15px; }
            
            #myVideo { width: 300%; left: -100%; }
        }
    </style>
    """, unsafe_allow_html=True)