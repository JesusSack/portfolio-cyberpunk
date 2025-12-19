import streamlit as st
import base64
import os

def get_base64_of_bin_file(bin_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, bin_file)
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def load_css(video_file="background.mp4"):
    
    bin_str = get_base64_of_bin_file(video_file)
    
    video_html = ""
    if bin_str:
        video_html = f'''
            <style>
                /* 1. FORZAR TRANSPARENCIA EN TODAS LAS CAPAS POSIBLES */
                .stApp {{
                    background: transparent !important;
                }}
                
                header, .stApp > header {{
                    background-color: transparent !important;
                }}

                /* Esta es la capa que suele tapar el video */
                .stAppViewContainer {{
                    background: transparent !important;
                    background-color: transparent !important;
                }}
                
                /* Por si acaso Streamlit usa IDs específicos */
                [data-testid="stAppViewContainer"] {{
                    background: transparent !important;
                }}
                
                [data-testid="stHeader"] {{
                    background: transparent !important;
                }}

                /* 2. EL VIDEO: POSICIÓN ABSOLUTA FIJA */
                #myVideo {{
                    position: fixed;
                    right: 0;
                    bottom: 0;
                    min-width: 100%; 
                    min-height: 100%;
                    width: auto; 
                    height: auto;
                    z-index: -1; /* Detrás del contenido */
                    object-fit: cover;
                }}
                
                /* 3. MÁSCARA OSCURA (Overlay) */
                #videoOverlay {{
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.75); /* Oscuridad */
                    z-index: 0; /* Encima del video */
                    pointer-events: none;
                }}
                
                /* 4. EL CONTENIDO (Texto, botones) DEBE ESTAR ARRIBA */
                .main {{
                    z-index: 1;
                    position: relative;
                }}
                
                [data-testid="stSidebar"] {{
                    z-index: 2;
                }}
            </style>
            
            <video autoplay muted loop playsinline id="myVideo">
                <source src="data:video/mp4;base64,{bin_str}" type="video/mp4">
            </video>
            <div id="videoOverlay"></div>
        '''
    else:
        st.error("No se encontró el video.")

    st.markdown(video_html, unsafe_allow_html=True)

    # ESTILOS ADICIONALES (TEXTO Y DECORACIÓN)
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');
        
        /* Texto base claro */
        body, .stMarkdown, p {{
            color: #e0e0e0 !important;
            font-family: 'Roboto Mono', monospace;
        }}

        /* Títulos */
        h1, h2, h3 {{ font-family: 'Orbitron', sans-serif !important; letter-spacing: 2px; text-transform: uppercase; }}
        h1 {{ color: #fff; text-shadow: 0 0 10px cyan; }}
        h2 {{ color: #F3F315; border-bottom: 2px solid #F3F315; }}
        h3 {{ color: #FF0055; }}

        /* GLITCH (Tu nombre) */
        @keyframes glitch-anim {{
            0% {{ clip-path: inset(50% 0 30% 0); transform: translate(-5px, 0); }}
            20% {{ clip-path: inset(20% 0 60% 0); transform: translate(5px, 0); }}
            40% {{ clip-path: inset(80% 0 5% 0); transform: translate(-5px, 0); }}
            60% {{ clip-path: inset(10% 0 70% 0); transform: translate(5px, 0); }}
            80% {{ clip-path: inset(40% 0 20% 0); transform: translate(-5px, 0); }}
            100% {{ clip-path: inset(30% 0 50% 0); transform: translate(5px, 0); }}
        }}
        .glitch-wrapper {{ font-family: 'Orbitron', sans-serif; font-size: 4rem; font-weight: 900; color: white; display: inline-block; position: relative; }}
        .glitch::before, .glitch::after {{ content: attr(data-text); position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: #050505; opacity: 0.8; }}
        .glitch::before {{ left: 2px; text-shadow: -2px 0 #ff00c1; clip: rect(44px, 450px, 56px, 0); animation: glitch-anim 5s infinite linear alternate-reverse; }}
        .glitch::after {{ left: -2px; text-shadow: -2px 0 #00fff9; clip: rect(44px, 450px, 56px, 0); animation: glitch-anim 2s infinite linear alternate-reverse; }}

        /* TARJETAS SEMI-TRANSPARENTES */
        .hero-card {{
            background: rgba(20, 20, 20, 0.6); 
            backdrop-filter: blur(5px);
            border: 1px solid #00ffff;
            padding: 30px; border-radius: 10px;
        }}
        
        .project-container {{
            background: rgba(10, 10, 10, 0.7);
            backdrop-filter: blur(5px);
            border: 1px solid #333;
            padding: 20px; border-radius: 5px;
            transition: 0.3s;
        }}
        .project-container:hover {{ border-color: #00ffff; transform: translateY(-5px); box-shadow: 0 0 20px rgba(0,255,255,0.3); }}

        /* SIDEBAR */
        [data-testid="stSidebar"] {{
            background-color: rgba(0, 0, 0, 0.9) !important;
            border-right: 1px solid #333;
        }}
        
        /* Enlaces */
        a {{ color: #F3F315 !important; text-decoration: none; }}
        .tech-chip {{ background: #111; border: 1px solid #333; color: cyan; padding: 2px 8px; margin-right: 5px; }}
    /* ... (toda tu configuración anterior) ... */

    /* === OPTIMIZACIÓN MOBILE === */
    @media only screen and (max-width: 768px) {
        /* 1. Ajustar el Título Glitch */
        .glitch-wrapper {
            transform: scale(0.6); /* Reducir al 60% */
            margin-left: -20px; /* Centrar visualmente */
        }
        
        .glitch {
            font-size: 2.5rem !important; /* Texto más chico */
        }

        /* 2. Ajustar márgenes del contenedor */
        .block-container {
            padding-top: 3rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        /* 3. Tarjetas más compactas */
        .cyber-card {
            padding: 15px;
        }
        
        .card-title {
            font-size: 1.2rem;
        }
        
        /* 4. Video de fondo en móviles */
        #myVideo {
            /* En algunos móviles el video fijo puede dar problemas, 
               esto asegura que cubra todo sin romperse */
            width: 300%; /* Más ancho para que no se corte al scrollear */
            left: -100%;
        }
    }
                </style>
    """, unsafe_allow_html=True)