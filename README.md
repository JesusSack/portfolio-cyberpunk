# ⚡ Cyberpunk 2025: Interactive AI & Data Portfolio

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/System-ONLINE-success?style=for-the-badge)

> **"I build end-to-end systems that feel like magic but run on pure logic."**

## 📂 System Overview

This repository contains the source code for my personal professional portfolio, designed as an immersive **Cyberpunk/Sci-Fi HUD interface**.

Unlike traditional static websites, this project leverages **Python and Streamlit** to create a dynamic web application. It features custom CSS injections, HTML5 components for audio processing, and a responsive design that works on both desktop and mobile neural-links.

### 🔗 Live Demo
[**>> ACCESS SYSTEM INTERFACE <<**](https://share.streamlit.io/)
*(Note: Replace this link after deploying to Streamlit Cloud)*

---

## 🛠️ Tech Stack & Features

### Core Technologies
* **Python 3.10+**: Core logic and backend scripting.
* **Streamlit**: Frontend framework for rapid data app development.
* **HTML5 / CSS3**: Custom "Holo-Deck" styling, glitched text effects, and animations.
* **JavaScript**: Custom audio player logic with playlist management and auto-looping.

### Key Modules
1.  **🎥 Dynamic Background**: Full-screen video loop with CSS masking overlays (transparent UI).
2.  **🔊 Sonic Module**: A custom-built Sidebar Music Player.
    * JavaScript-based audio control.
    * Playlist support (Auto-looping 3 tracks).
    * Visual equalizer animation.
3.  **💻 HUD Interface**:
    * **Terminal Header**: Bio section styled as a system boot log.
    * **Project Cards**: Holographic glassmorphism effects with varying neon color codes based on tech domain (AI, Vision, Data, BI).
4.  **📱 Mobile Responsive**: Adaptive CSS media queries for optimized viewing on smartphones.

---

## ⚙️ Local Initialization

To run this system on your local machine, follow these protocols:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/JesusSack/portfolio-cyberpunk.git](https://github.com/JesusSack/portfolio-cyberpunk.git)
    cd portfolio-cyberpunk
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the App**
    ```bash
    streamlit run main.py
    ```

---

## 📂 File Structure

```text
/portfolio-root
│
├── main.py             # Entry point (Main Layout)
├── styles.py           # CSS Injection & Mobile Optimization
├── header.py           # Terminal Header Logic
├── header.html         # HTML Template for the Header
├── sidebar.py          # Sidebar, Profile Pic & Audio Player
├── projects.py         # Holographic Project Cards
│
├── .streamlit/
│   └── config.toml     # Dark Mode & Server Config
│
├── assets/             # (Optional folder for organization)
│   ├── background.mp4  # 10MB+ Loop Video
│   ├── profile.jpg     # Profile Picture
│   ├── track1.mp3      # Audio Track 1
│   ├── track2.mp3      # Audio Track 2
│   └── track3.mp3      # Audio Track 3
│
├── requirements.txt    # Python Dependencies
└── README.md           # Documentation  



Operator Identity
JESÚS SACK

Role: AI & Data Engineer // Backend Specialist

Base: Rosario, Argentina

Focus: Machine Learning, Deep Learning, ETL Pipelines.

<img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin"> <img src="https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github">

<p align="center"> <i>END OF LINE. © 2025</i> </p>



