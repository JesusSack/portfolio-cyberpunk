import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# --- FUNCIÓN PARA CARGAR AUDIO ---
def get_base64_audio(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def get_base64_image(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def show_sidebar():
    with st.sidebar:
        t1 = get_base64_audio("track1.mp3")
        t2 = get_base64_audio("track2.mp3")
        t3 = get_base64_audio("track3.mp3")
        
        if t1:
            if not t2: t2 = t1 
            if not t3: t3 = t1
            
            st.markdown("### 🔊 SONIC MODULE")
            
            cyber_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
                body {{ background: transparent; margin: 0; padding: 5px; overflow: hidden; font-family: 'Orbitron', sans-serif; }}
                
                .cyber-audio-controls {{ 
                    border: 1px solid #00ffff; 
                    background: rgba(0, 20, 20, 0.9); 
                    padding: 10px; 
                    border-radius: 5px; 
                    text-align: center; 
                    box-shadow: 0 0 10px rgba(0, 255, 255, 0.2); 
                }}
                
                #cyber-btn {{ 
                    background: transparent; 
                    border: 2px solid #F3F315; 
                    color: #F3F315; 
                    font-family: 'Orbitron', sans-serif; 
                    font-size: 14px; 
                    padding: 8px 0; 
                    cursor: pointer; 
                    width: 100%; 
                    transition: 0.2s; 
                    text-transform: uppercase; 
                    font-weight: bold; 
                    margin-bottom: 5px; 
                }}
                
                #cyber-btn:hover {{ background: #F3F315; color: #000; box-shadow: 0 0 15px #F3F315; transform: scale(1.02); }}
                
                .track-display {{
                    font-size: 10px;
                    color: #00ffff;
                    margin-bottom: 8px;
                    letter-spacing: 1px;
                }}
                
                .equalizer {{ display: flex; justify-content: center; gap: 4px; height: 20px; align-items: flex-end; }}
                .bar {{ width: 6px; background: #333; height: 5px; transition: height 0.1s; }}
                
                .active .bar {{ background: #FF0055; box-shadow: 0 0 5px #FF0055; animation: bounce 0.6s infinite ease-in-out alternate; }}
                .active .bar:nth-child(1) {{ animation-delay: 0.1s; }} .active .bar:nth-child(2) {{ animation-delay: 0.3s; }}
                .active .bar:nth-child(3) {{ animation-delay: 0.5s; }} .active .bar:nth-child(4) {{ animation-delay: 0.2s; }}
                .active .bar:nth-child(5) {{ animation-delay: 0.4s; }}
                
                @keyframes bounce {{ 0% {{ height: 5px; }} 100% {{ height: 20px; }} }}
            </style>
            </head>
            <body>
                <audio id="cyber-player"></audio>
                
                <div class="cyber-audio-controls">
                    <div class="track-display" id="track-info">SYSTEM READY</div>
                    <button id="cyber-btn" onclick="toggleAudio()">▶ INITIALIZE</button>
                    <div class="equalizer" id="eq">
                        <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                    </div>
                </div>

                <script>
                    const playlist = [
                        "data:audio/mp3;base64,{t1}",
                        "data:audio/mp3;base64,{t2}",
                        "data:audio/mp3;base64,{t3}"
                    ];
                    
                    var currentTrack = 0;
                    var audio = document.getElementById("cyber-player");
                    var btn = document.getElementById("cyber-btn");
                    var eq = document.getElementById("eq");
                    var info = document.getElementById("track-info");
                    var isPlaying = false;
                    
                    audio.volume = 0.4;
                    audio.src = playlist[currentTrack];

                    function toggleAudio() {{
                        if (isPlaying) {{
                            audio.pause();
                            btn.innerText = "▶ RESUME";
                            btn.style.borderColor = "#F3F315";
                            btn.style.color = "#F3F315";
                            eq.classList.remove("active");
                            info.innerText = "PAUSED";
                            isPlaying = false;
                        }} else {{
                            audio.play();
                            updateButtonState();
                        }}
                    }}
                    
                    function updateButtonState() {{
                        btn.innerText = "❚❚ TERMINATE";
                        btn.style.borderColor = "#FF0055";
                        btn.style.color = "#FF0055";
                        eq.classList.add("active");
                        info.innerText = "AUDIO STREAM ACTIVE"; 
                        isPlaying = true;
                    }}

                    audio.addEventListener('ended', function() {{
                        currentTrack++;
                        if (currentTrack >= playlist.length) {{
                            currentTrack = 0;
                        }}
                        audio.src = playlist[currentTrack];
                        audio.play();
                        updateButtonState();
                    }});
                </script>
            </body>
            </html>
            """
            components.html(cyber_html, height=150)
        else:
            st.error("⚠️ SYSTEM ERROR: Missing 'track1.mp3'")

        img_b64 = get_base64_image("profile.jpg")
        if not img_b64:
            img_b64 = get_base64_image("profile.png")
            
        img_html = ""
        if img_b64:
            img_html = f'<img src="data:image/png;base64,{img_b64}" class="profile-pic">'

        st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;700&display=swap');
            
            /* ID CARD & PROFILE PIC */
            .id-card {
                border: 2px solid #00ffff;
                background: linear-gradient(135deg, rgba(0,255,255,0.1) 0%, rgba(0,0,0,0) 100%);
                padding: 20px; 
                text-align: center; 
                margin-bottom: 20px;
                box-shadow: 0 0 15px rgba(0, 255, 255, 0.2);
                /* Ajuste para que la tarjeta se achique si solo tiene foto */
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            .profile-pic {
                width: 120px; /* Un poco más grande ahora que está sola */
                height: 120px;
                border-radius: 50%;
                border: 3px solid #00ffff;
                object-fit: cover;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.6);
            }

            /* TERMINAL STATUS */
            .terminal-box {
                background: #0a0a0a; border-left: 4px solid #00ff00;
                padding: 10px; font-family: 'Roboto Mono', monospace;
                font-size: 0.85rem; color: #00ff00; margin-bottom: 20px;
            }
            .blink { animation: blinker 1.5s linear infinite; }
            @keyframes blinker { 50% { opacity: 0; } }

            /* DATALINK BUTTONS */
            .link-container { margin-bottom: 20px; }
            .cyber-link {
                display: block; background: transparent; border: 1px solid #333;
                color: #c0c0c0 !important; padding: 10px; margin-bottom: 8px;
                text-decoration: none !important; font-family: 'Orbitron', sans-serif;
                font-size: 0.9rem; transition: all 0.3s ease; position: relative; overflow: hidden;
            }
            .cyber-link:before {
                content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 0, 85, 0.2), transparent); transition: 0.5s;
            }
            .cyber-link:hover {
                border-color: #FF0055; color: #fff !important; padding-left: 20px;
                text-shadow: 0 0 8px #FF0055; box-shadow: 0 0 10px rgba(255, 0, 85, 0.2);
            }
            .cyber-link:hover:before { left: 100%; }

            /* CHIPS */
            .stack-section { margin-bottom: 15px; }
            .stack-title { color: #F3F315; font-family: 'Orbitron', sans-serif; font-size: 0.8rem; margin-bottom: 5px; border-bottom: 1px solid #333; }
            .chip-container { display: flex; flex-wrap: wrap; gap: 5px; }
            .cyber-chip {
                background: #111; border: 1px solid #444; color: #00ffff;
                padding: 4px 8px; font-size: 0.75rem; font-family: 'Roboto Mono', monospace;
                border-radius: 3px; transition: all 0.2s; cursor: default;
            }
            .cyber-chip:hover {
                transform: translateY(-3px) scale(1.05); border-color: #00ffff;
                background: rgba(0, 255, 255, 0.1); box-shadow: 0 0 10px #00ffff; color: #fff;
            }
        </style>
        """, unsafe_allow_html=True)

        if img_html:
            st.markdown(f"""
            <div class="id-card">
                {img_html}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""<div class="terminal-box"><div>📍 BASE: Rosario, ARG</div><div style="margin-top: 5px;"><span class="blink">🔋</span> STATUS: <span style="color: #fff;">Available for Dev</span></div></div>""", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📡 DATALINK")
        st.markdown("""
        <div class="link-container">
            <a href="https://wa.me/5493415151411" target="_blank" class="cyber-link">📞 WHATSAPP SECURE</a>
            <a href="mailto:jesusmsack@hotmail.com" class="cyber-link">📧 ENCRYPTED MAIL</a>
            <a href="https://www.linkedin.com/in/jesus05/" target="_blank" class="cyber-link">🔗 LINKEDIN PROFILE</a>
            <a href="https://github.com/JesusSack" target="_blank" class="cyber-link">🐙 GITHUB REPO</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 💾 COMPLETE TECH STACK")
        
        def draw_tech_block(title, techs):
            chips_html = "".join([f'<span class="cyber-chip">{t}</span>' for t in techs])
            st.markdown(f"""<div class="stack-section"><div class="stack-title">{title}</div><div class="chip-container">{chips_html}</div></div>""", unsafe_allow_html=True)

        draw_tech_block("LANGUAGES", ["PYTHON 3.10+", "SQL", "BASH"])
        draw_tech_block("AI & VISION", ["OPENAI GPT-4o", "WHISPER", "YOLOv8", "OPENCV", "MULTIPROCESSING"])
        draw_tech_block("DATA & CLOUD", ["GCP", "BIGQUERY", "AWS S3 / BOTO3", "SQL SERVER", "SHEETS API"])
        draw_tech_block("TOOLS & LIBS", ["STREAMLIT", "PANDAS", "SQLALCHEMY", "BS4", "GITHUB ACTIONS", "POWER BI"])