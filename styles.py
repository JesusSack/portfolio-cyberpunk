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
        /* 6. OPTIMIZACIÓN MÓVIL (FLECHA LARGA) */
        /* ================================================= */
        @media only screen and (max-width: 768px) {
            
            /* INSTRUCCIÓN DE MENÚ MEJORADA */
            .glitch-wrapper::before {
                /* Flecha larga construida con caracteres */
                content: "↖--------- MENU: PRESIONE AQUÍ"; 
                
                display: block;
                position: absolute;
                top: -50px;       /* Más arriba para acercarse al botón */
                left: -40px;      /* Bien a la izquierda */
                width: 120%;      /* Ancho extra para que no se corte */
                text-align: left; /* Alineado a la izquierda */
                
                /* Estilo del texto */
                color: #F3F315;   /* Amarillo Cyberpunk */
                font-family: 'Orbitron', sans-serif;
                font-size: 1.3rem; /* Letra MÁS GRANDE */
                font-weight: 900;  /* Más gruesa */
                letter-spacing: 1px;
                text-shadow: 0 0 10px #F3F315; /* Más brillo */
                
                animation: blinker 1.5s infinite alternate;
            }

            @keyframes blinker { 
                0% { opacity: 0.4; text-shadow: 0 0 5px #F3F315; }
                100% { opacity: 1; text-shadow: 0 0 20px #F3F315, 0 0 10px #FF0055; }
            }

            /* Ajustes del nombre principal para dar espacio */
            .glitch-wrapper {
                transform: scale(0.65);
                margin-top: 40px; /* Bajamos el nombre para dejar sitio a la flecha */
                margin-left: -15px;
            }

            .glitch { font-size: 2.5rem !important; }
            
            .block-container { padding-top: 5rem !important; }

            .cyber-card { padding: 15px; }
            
            #myVideo { width: 300%; left: -100%; }
        }
    </style>
    """, unsafe_allow_html=True)