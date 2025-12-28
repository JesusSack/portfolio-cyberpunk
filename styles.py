import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

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

        button[kind="header"] {
            z-index: 100000 !important;
            background: transparent !important;
            color: #00ffff !important;
        }

        ::-webkit-scrollbar { width: 10px; background: #111; }
        ::-webkit-scrollbar-thumb { background: #00ffff; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #FF0055; }

        @media only screen and (max-width: 768px) {
            
            .glitch-wrapper::before {
                content: "↖----------- MENU: PRESIONE AHÍ"; 
                display: block;
                position: absolute;
                top: -115px;        
                left: 10px;
                width: 300px; 
                text-align: left;
                color: #F3F315;
                font-family: 'Orbitron', sans-serif;
                font-size: 1.3rem; 
                font-weight: 900;
                letter-spacing: 2px; 
                text-shadow: 0 0 10px #F3F315;
                animation: blinker 1.5s infinite alternate;
                pointer-events: none; 
            }

            @keyframes blinker { 
                0% { opacity: 0.4; text-shadow: 0 0 5px #F3F315; }
                100% { opacity: 1; text-shadow: 0 0 20px #F3F315, 0 0 10px #FF0055; }
            }

            .glitch-wrapper {
                transform: scale(0.65);
                margin-top: 70px; 
                margin-left: -10px;
            }

            .glitch { font-size: 2.5rem !important; }
            
            .block-container { padding-top: 6rem !important; }

            .cyber-card { padding: 15px; }
            
            #myVideo { width: 300%; left: -100%; }
        }
    </style>
    """, unsafe_allow_html=True)
