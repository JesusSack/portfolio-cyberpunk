# ⚡ Cyberpunk Portfolio OS | AI & Data Engineer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

> **"Not just a website, but an interactive system."** > This project is a production-level web application that serves as my professional portfolio. It features a modular architecture, a built-in AI Agent for recruiting queries, and a custom "Cyberpunk" aesthetic engineered via CSS injection.

---

## 🤖 New Feature: AI Neural Agent (RAG)
I have integrated a **Retrieval-Augmented Generation (RAG)** agent directly into the portfolio.
* **Architecture:** The agent (`agent.py`) connects to the **OpenAI API** using a secure secrets management system.
* **Context Awareness:** It utilizes a static knowledge base (`context.py`) containing my full CV, technical stack, and project history.
* **Functionality:** Visitors can "interview" the portfolio. The agent detects language (EN/ES), formats contact links, and answers technical queries about my experience.

---

## 🛠️ Technical Architecture

The system follows a **Modular Micro-component** pattern to ensure maintainability and scalability:

```text
📂 portfolio-cyberpunk/
├── 📄 main.py           # Core Application Orchestrator (Tabs & Layout)
├── 📄 agent.py          # AI Logic & Chat Interface (GPT Integration)
├── 📄 context.py        # Static Knowledge Base (Data Context for RAG)
├── 📄 styles.py         # CSS Engine (Responsive Design & Animations)
├── 📄 sidebar.py        # Navigation Component
├── 📄 projects.py       # Project Gallery Module
└── 📄 requirements.txt  # Dependency Management


Key Engineering Highlights
Frontend-as-Code: Used Streamlit st.markdown to inject custom CSS/HTML, bypassing framework limitations to create a unique HUD experience.

Base64 Media Pipeline: Implemented a local data pipeline to encode video/audio assets into Base64 strings, ensuring zero-latency loading without external CDNs.

Responsive Engine: Advanced CSS media queries to handle mobile layouts (custom menu positioning and touch-optimized interactions).

CI/CD: Automated deployment pipeline via Streamlit Cloud linked to GitHub.


🚀 Installation & Local Setup
To run this AI-powered portfolio locally, follow these steps:

1. Clone the repository
   git clone [https://github.com/JesusSack/portfolio-cyberpunk.git](https://github.com/JesusSack/portfolio-cyberpunk.git)
cd portfolio-cyberpunk

¡Excelente idea! Un README.md actualizado es vital porque es la portada técnica de tu proyecto. Cuando un reclutador entre a tu GitHub, esto es lo primero que leerá.

Vamos a transformar el README para que no solo diga "es una web", sino que destaque la Arquitectura Modular, la Integración de IA (RAG) y el Diseño Responsivo Avanzado.

Copia y pega el siguiente código en tu archivo README.md.

📄 Nuevo README.md (Optimizado para Ingeniería de Datos e IA)
Markdown

# ⚡ Cyberpunk Portfolio OS | AI & Data Engineer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

> **"Not just a website, but an interactive system."** > This project is a production-level web application that serves as my professional portfolio. It features a modular architecture, a built-in AI Agent for recruiting queries, and a custom "Cyberpunk" aesthetic engineered via CSS injection.

---

## 🤖 New Feature: AI Neural Agent (RAG)
I have integrated a **Retrieval-Augmented Generation (RAG)** agent directly into the portfolio.
* **Architecture:** The agent (`agent.py`) connects to the **OpenAI API** using a secure secrets management system.
* **Context Awareness:** It utilizes a static knowledge base (`context.py`) containing my full CV, technical stack, and project history.
* **Functionality:** Visitors can "interview" the portfolio. The agent detects language (EN/ES), formats contact links, and answers technical queries about my experience.

---

## 🛠️ Technical Architecture

The system follows a **Modular Micro-component** pattern to ensure maintainability and scalability:

```text
📂 portfolio-cyberpunk/
├── 📄 main.py           # Core Application Orchestrator (Tabs & Layout)
├── 📄 agent.py          # AI Logic & Chat Interface (GPT Integration)
├── 📄 context.py        # Static Knowledge Base (Data Context for RAG)
├── 📄 styles.py         # CSS Engine (Responsive Design & Animations)
├── 📄 sidebar.py        # Navigation Component
├── 📄 projects.py       # Project Gallery Module
└── 📄 requirements.txt  # Dependency Management
Key Engineering Highlights
Frontend-as-Code: Used Streamlit st.markdown to inject custom CSS/HTML, bypassing framework limitations to create a unique HUD experience.

Base64 Media Pipeline: Implemented a local data pipeline to encode video/audio assets into Base64 strings, ensuring zero-latency loading without external CDNs.

Responsive Engine: Advanced CSS media queries to handle mobile layouts (custom menu positioning and touch-optimized interactions).

CI/CD: Automated deployment pipeline via Streamlit Cloud linked to GitHub.

🚀 Installation & Local Setup
To run this AI-powered portfolio locally, follow these steps:

1. Clone the repository
Bash

git clone [https://github.com/JesusSack/portfolio-cyberpunk.git](https://github.com/JesusSack/portfolio-cyberpunk.git)
cd portfolio-cyberpunk

2. Install Dependencies
   pip install -r requirements.txt

3. Configure Secrets (Crucial for AI)
Create a .streamlit/secrets.toml file in the root directory to store your API Key safely:
# .streamlit/secrets.toml
   OPENAI_API_KEY = "sk-your-openai-api-key-here"   

4. Run the Application
   streamlit run main.py

¡Excelente idea! Un README.md actualizado es vital porque es la portada técnica de tu proyecto. Cuando un reclutador entre a tu GitHub, esto es lo primero que leerá.

Vamos a transformar el README para que no solo diga "es una web", sino que destaque la Arquitectura Modular, la Integración de IA (RAG) y el Diseño Responsivo Avanzado.

Copia y pega el siguiente código en tu archivo README.md.

📄 Nuevo README.md (Optimizado para Ingeniería de Datos e IA)
Markdown

# ⚡ Cyberpunk Portfolio OS | AI & Data Engineer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

> **"Not just a website, but an interactive system."** > This project is a production-level web application that serves as my professional portfolio. It features a modular architecture, a built-in AI Agent for recruiting queries, and a custom "Cyberpunk" aesthetic engineered via CSS injection.

---

## 🤖 New Feature: AI Neural Agent (RAG)
I have integrated a **Retrieval-Augmented Generation (RAG)** agent directly into the portfolio.
* **Architecture:** The agent (`agent.py`) connects to the **OpenAI API** using a secure secrets management system.
* **Context Awareness:** It utilizes a static knowledge base (`context.py`) containing my full CV, technical stack, and project history.
* **Functionality:** Visitors can "interview" the portfolio. The agent detects language (EN/ES), formats contact links, and answers technical queries about my experience.

---

## 🛠️ Technical Architecture

The system follows a **Modular Micro-component** pattern to ensure maintainability and scalability:

```text
📂 portfolio-cyberpunk/
├── 📄 main.py           # Core Application Orchestrator (Tabs & Layout)
├── 📄 agent.py          # AI Logic & Chat Interface (GPT Integration)
├── 📄 context.py        # Static Knowledge Base (Data Context for RAG)
├── 📄 styles.py         # CSS Engine (Responsive Design & Animations)
├── 📄 sidebar.py        # Navigation Component
├── 📄 projects.py       # Project Gallery Module
└── 📄 requirements.txt  # Dependency Management
Key Engineering Highlights
Frontend-as-Code: Used Streamlit st.markdown to inject custom CSS/HTML, bypassing framework limitations to create a unique HUD experience.

Base64 Media Pipeline: Implemented a local data pipeline to encode video/audio assets into Base64 strings, ensuring zero-latency loading without external CDNs.

Responsive Engine: Advanced CSS media queries to handle mobile layouts (custom menu positioning and touch-optimized interactions).

CI/CD: Automated deployment pipeline via Streamlit Cloud linked to GitHub.

🚀 Installation & Local Setup
To run this AI-powered portfolio locally, follow these steps:

1. Clone the repository
Bash

git clone [https://github.com/JesusSack/portfolio-cyberpunk.git](https://github.com/JesusSack/portfolio-cyberpunk.git)
cd portfolio-cyberpunk
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Configure Secrets (Crucial for AI)
Create a .streamlit/secrets.toml file in the root directory to store your API Key safely:

Ini, TOML

# .streamlit/secrets.toml
OPENAI_API_KEY = "sk-your-openai-api-key-here"
4. Run the Application
Bash

streamlit run main.py
📱 Mobile Optimization
The system includes specific overrides for mobile devices:

Adaptive Layout: The DOM structure realigns for vertical viewports.

Touch UX: Menu buttons and interactive elements are resized for touch targets.

Visual Guide: Added a "Presione Aquí" directional indicator for the mobile menu to improve User Experience (UX).


📬 Contact
LinkedIn: Jesus Sack

Email: jesusmsack@hotmail.com

Built with ❤️ and 🐍 Python by Jesús Sack.




