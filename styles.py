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
                content: "↖";
                display: block;
                position: absolute;
                top: -160px;
                left: -15px;
                font-size: 7rem;
                line-height: 1;
                color: #F3F315;
                text-shadow: 0 0 25px #F3F315;
                animation: blinker 1.2s infinite alternate;
                pointer-events: none;
                z-index: 999999;
            }

            .glitch-wrapper::after {
                content: "MENU:\A PRESIONE AHÍ";
                white-space: pre;
                display: block;
                position: absolute;
                top: -100px;
                left: 75px;
                width: 250px;
                text-align: left;
                font-family: 'Orbitron', sans-serif;
                font-size: 1.6rem; 
                font-weight: 900;
                line-height: 1.2;
                letter-spacing: 1px;
                color: #F3F315;
                text-shadow: 0 0 15px #F3F315;
                animation: blinker 1.2s infinite alternate;
                pointer-events: none;
                z-index: 999999;
            }

            @keyframes blinker { 
                0% { opacity: 0.6; text-shadow: 0 0 10px #F3F315; }
                100% { opacity: 1; text-shadow: 0 0 30px #F3F315, 0 0 10px #FF0055; }
            }

            .glitch-wrapper {
                transform: scale(0.65);
                margin-top: 110px;
                margin-left: -10px;
            }

            .glitch { font-size: 2.5rem !important; }
            
            .block-container { padding-top: 6rem !important; }

            .cyber-card { padding: 15px; }
            
            #myVideo { width: 300%; left: -100%; }
        }
    </style>
    """, unsafe_allow_html=True)
