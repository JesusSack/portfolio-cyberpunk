import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

        [data-testid="stSidebarCollapsedControl"] svg {
            display: none !important;
        }

        [data-testid="stSidebarCollapsedControl"] {
            width: auto !important;
            padding: 5px 15px !important;
            border: 2px solid #F3F315 !important;
            background-color: rgba(10, 10, 10, 0.9) !important;
            border-radius: 0px !important;
            margin-top: 5px;
            margin-left: 5px;
            box-shadow: 0 0 10px rgba(243, 243, 21, 0.2);
            transition: all 0.3s ease;
        }

        [data-testid="stSidebarCollapsedControl"]::after {
            content: "☰ MENU"; 
            font-family: 'Orbitron', sans-serif;
            color: #F3F315;
            font-weight: 900;
            font-size: 1rem;
            letter-spacing: 2px;
        }

        [data-testid="stSidebarCollapsedControl"]:hover {
            box-shadow: 0 0 20px rgba(243, 243, 21, 0.6);
            background-color: rgba(243, 243, 21, 0.1) !important;
            border-color: #fff !important;
        }

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

        ::-webkit-scrollbar { width: 10px; background: #111; }
        ::-webkit-scrollbar-thumb { background: #00ffff; border-radius: 5px; }
        ::-webkit-scrollbar-thumb:hover { background: #FF0055; }

        @media only screen and (max-width: 768px) {
            
            .glitch-wrapper {
                transform: scale(0.65);
                margin-top: 50px; 
                margin-left: -10px;
            }

            .glitch { font-size: 2.5rem !important; }
            
            .block-container { padding-top: 6rem !important; }

            .cyber-card { padding: 15px; }
            
            #myVideo { width: 300%; left: -100%; }
        }
    </style>
    """, unsafe_allow_html=True)
