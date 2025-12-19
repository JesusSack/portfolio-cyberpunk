import streamlit as st

def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');

        #myVideo {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
            opacity: 0.6;
        }

        .stApp {
            background: rgba(0, 0, 0, 0.7);
        }

        header {visibility: hidden;}
        footer {visibility: hidden;}

        .block-container {
            padding-top: 1rem;
            padding-bottom: 5rem;
        }

        section[data-testid="stSidebar"] {
            z-index: 99999 !important;
            background-color: #0a0a0a !important;
        }

        button[kind="header"] {
            z-index: 100000 !important;
        }

        ::-webkit-scrollbar {
            width: 10px;
            background: #111;
        }

        ::-webkit-scrollbar-thumb {
            background: #00ffff;
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #FF0055;
        }

        @media only screen and (max-width: 768px) {
            .glitch-wrapper {
                transform: scale(0.6);
                margin-left: -20px;
            }

            .glitch {
                font-size: 2.5rem !important;
            }

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