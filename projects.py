import streamlit as st

def show_projects():
    # CSS AVANZADO (ESTILOS VISUALES)
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

        /* BASE CARD */
        .cyber-card {
            background: rgba(10, 15, 20, 0.85);
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 10px;
            position: relative;
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        .cyber-card:hover { transform: translateY(-5px); z-index: 10; }

        /* TYPOGRAPHY */
        .card-title { font-family: 'Orbitron', sans-serif; font-size: 1.8rem; font-weight: 800; margin-bottom: 5px; text-transform: uppercase; }
        .card-meta { font-family: 'Share Tech Mono', monospace; font-size: 0.9rem; color: #ccc; margin-bottom: 15px; display: flex; gap: 15px; }
        .card-desc { font-family: 'Roboto Mono', monospace; font-size: 1rem; line-height: 1.5; color: #e0e0e0; margin-bottom: 25px; flex-grow: 1; }

        /* HUD BUTTONS */
        .hud-btn {
            display: inline-block;
            padding: 8px 20px;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.85rem;
            text-decoration: none !important;
            border: 1px solid;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            width: fit-content;
            font-weight: bold;
            position: relative;
            background: rgba(0,0,0,0.3);
        }
        .hud-btn:hover { background: currentColor; color: #000 !important; box-shadow: 0 0 15px currentColor; cursor: pointer; }
        .hud-icon { margin-right: 8px; }

        /* COLORS */
        /* CORTEX (CYAN) */
        .style-cortex { border-left: 6px solid #00ffff; box-shadow: 0 0 10px rgba(0, 255, 255, 0.1); }
        .style-cortex:hover { box-shadow: 0 0 25px rgba(0, 255, 255, 0.4); border-color: #00ffff; }
        .style-cortex .card-title { color: #fff; text-shadow: 0 0 10px #00ffff; }
        .style-cortex .card-badge { color: #00ffff; border: 1px solid #00ffff; padding: 2px 8px; }
        .btn-cyan { color: #00ffff !important; border-color: #00ffff; }

        /* VISION (PINK) */
        .style-vision { border-right: 6px solid #FF0055; border-bottom: 1px solid #FF0055; box-shadow: 0 0 10px rgba(255, 0, 85, 0.1); }
        .style-vision:hover { box-shadow: 0 0 25px rgba(255, 0, 85, 0.4); }
        .style-vision .card-title { color: #FF0055; text-shadow: 0 0 5px #FF0055; }
        .style-vision .card-badge { color: #FF0055; border: 1px solid #FF0055; padding: 2px 8px; }
        .btn-pink { color: #FF0055 !important; border-color: #FF0055; }

        /* HAZARD (YELLOW) */
        .style-hazard { border-top: 4px solid #F3F315; }
        .style-hazard:hover { box-shadow: 0 0 25px rgba(243, 243, 21, 0.3); }
        .style-hazard .card-title { color: #F3F315; }
        .style-hazard .card-badge { background: #F3F315; color: #000; padding: 2px 8px; font-weight: bold; }
        .btn-yellow { color: #F3F315 !important; border-color: #F3F315; }

        /* MATRIX (GREEN) */
        .style-matrix { border: 1px solid #00ff00; box-shadow: inset 0 0 20px rgba(0, 255, 0, 0.1); }
        .style-matrix:hover { box-shadow: inset 0 0 40px rgba(0, 255, 0, 0.2), 0 0 15px #00ff00; }
        .style-matrix .card-title { color: #00ff00; font-family: 'Share Tech Mono', monospace; }
        .style-matrix .card-badge { color: #00ff00; border-bottom: 1px solid #00ff00; padding: 2px 8px; }
        .btn-green { color: #00ff00 !important; border-color: #00ff00; }

        .scanline {
            width: 100%; height: 100px; z-index: 0;
            background: linear-gradient(0deg, rgba(0,0,0,0) 0%, rgba(255, 255, 255, 0.03) 50%, rgba(0,0,0,0) 100%);
            opacity: 0.1; position: absolute; bottom: 100%;
            animation: scanline 10s linear infinite; pointer-events: none;
        }
        @keyframes scanline { 0% { bottom: 100%; } 100% { bottom: -100%; } }
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO PRINCIPAL ---
    st.markdown("<h2 style='text-align: center; margin-bottom: 40px;'>📂 PROJECT DATABASE</h2>", unsafe_allow_html=True)

    # PROJECT 1: AI (CORTEX)
    with st.container():
        st.markdown("""
        <div class="cyber-card style-cortex">
            <div class="scanline"></div>
            <div class="card-meta">
                <span class="card-badge">ID: AI-01</span>
                <span>📅 2025</span>
                <span>👤 FULL STACK AI</span>
            </div>
            <div class="card-title">AI MULTIMODAL INTELLIGENCE</div>
            <div class="card-desc">
                Strategic surveillance system capable of seeing, listening, and reading. 
                Powered by <b>GPT-4o</b> for vision and <b>Whisper</b> for real-time audio analysis.
            </div>
            <a href="https://github.com/JesusSack/Proyecto_IA_Automation" target="_blank" class="hud-btn btn-cyan">
                <span class="hud-icon">⚡</span> SOURCE_CODE :: GITHUB
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([0.05, 0.95])
        with col2:
            with st.expander("➕ ACCESS TECHNICAL LOGS [AI-01]"):
                st.markdown("""
                - **Web Scraping:** `BeautifulSoup` with noise reduction algorithms.
                - **Models:** Multimodal integration (Text + Audio + Image).
                - **Backend:** Batch processing via Google Sheets API.
                - **Frontend:** Interactive Streamlit dashboard.
                """)
    
    st.write("") 
    with st.container():
        st.markdown("""
        <div class="cyber-card style-vision">
            <div class="card-meta">
                <span class="card-badge">ID: CV-8</span>
                <span>📅 2025</span>
                <span>👤 CV ENGINEER</span>
            </div>
            <div class="card-title">ADVANCED VISION & TELEMETRY</div>
            <div class="card-desc">
                Zero-latency RTSP streaming architecture. 
                Detects human poses and calculates biomechanical angles using <b>YOLOv8</b>.
            </div>
            <a href="https://github.com/JesusSack/desafio-vision" target="_blank" class="hud-btn btn-pink">
                <span class="hud-icon">👁️</span> SOURCE_CODE :: GITHUB
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([0.05, 0.95])
        with col2:
            with st.expander("➕ ACCESS TECHNICAL LOGS [CV-8]"):
                st.markdown("""
                - **Core:** Human Activity Recognition (HAR).
                - **Optimization:** Circular buffer + Threading for zero latency.
                - **Hardware:** Multiprocessing (3 CPU cores).
                - **Cloud:** Asynchronous upload to AWS S3.
                """)

    st.write("")
    # PROJECT 3: DATA ENG (HAZARD YELLOW)
    with st.container():
        st.markdown("""
        <div class="cyber-card style-hazard">
            <div class="card-meta">
                <span class="card-badge">WARNING: FINANCIAL DATA</span>
                <span>📅 2025</span>
                <span>👤 DATA ENGINEER</span>
            </div>
            <div class="card-title">SERVERLESS CRYPTO PIPELINE</div>
            <div class="card-desc">
                100% automated financial data ingestion. Modern serverless architecture 
                managed by event-driven triggers and CI/CD pipelines.
            </div>
            <a href="https://github.com/JesusSack/Proyecto_Crypto_ETL" target="_blank" class="hud-btn btn-yellow">
                <span class="hud-icon">⚠️</span> SOURCE_CODE :: GITHUB
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([0.05, 0.95])
        with col2:
            with st.expander("➕ ACCESS TECHNICAL LOGS [ETL]"):
                st.markdown("""
                - **Orchestration:** GitHub Actions (Cron Jobs).
                - **Warehouse:** Google BigQuery.
                - **Security:** Secret Management & Encrypted Service Accounts.
                - **Vis:** Native connection to Looker Studio.
                """)

    st.write("")
    # PROJECT 4: BI (MATRIX GREEN)
    with st.container():
        st.markdown("""
        <div class="cyber-card style-matrix">
            <div class="card-meta">
                <span class="card-badge">SYSTEM: RETAIL</span>
                <span>📅 2025</span>
                <span>👤 BI DEVELOPER</span>
            </div>
            <div class="card-title">DATASHOP WAREHOUSE</div>
            <div class="card-desc">
                Dimensional modeling (Star Schema) to transform raw data into 
                actionable business intelligence.
            </div>
            <a href="https://github.com/JesusSack/datashop-retail-etl" target="_blank" class="hud-btn btn-green">
                <span class="hud-icon">💾</span> SOURCE_CODE :: GITHUB
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([0.05, 0.95])
        with col2:
            with st.expander("➕ ACCESS TECHNICAL LOGS [BI]"):
                st.markdown("""
                - **DB:** SQL Server + Stored Procedures.
                - **Python:** Advanced ETL with Pandas and SQLAlchemy.
                - **Logic:** Surrogate Keys and MERGE statements.
                - **Dashboard:** Power BI with complex DAX metrics.
                """)

    st.markdown("---")
    st.markdown("<center><p style='font-family: Orbitron; color: #555; font-size: 0.8rem;'>END OF LINE. © 2025 JESÚS SACK</p></center>", unsafe_allow_html=True)