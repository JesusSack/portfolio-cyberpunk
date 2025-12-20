# ⚡ Cyberpunk Portfolio OS | AI & Data Engineer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)

> **"Not just a website, but an interactive system."**  
> Production-level web application designed as a professional portfolio, featuring a modular architecture, an embedded AI agent for recruiting queries, and a custom **Cyberpunk** aesthetic engineered via CSS injection.

---

## 🤖 AI Neural Agent (RAG)

This portfolio integrates a **Retrieval-Augmented Generation (RAG)** agent directly into the application.

- **Architecture:** The agent (`agent.py`) connects to the **OpenAI API** using secure secrets management.
- **Context Awareness:** A static knowledge base (`context.py`) contains my CV, technical stack, and project history.
- **Functionality:** Visitors can interact with the portfolio as if it were an interview. The agent detects language (EN/ES), formats contact links, and answers technical questions about my experience.

---

## 🛠️ Technical Architecture

The system follows a **Modular Micro-Component** pattern to ensure maintainability and scalability.

```text
📂 portfolio-cyberpunk/
├── 📄 main.py           # Core application orchestrator (layout & tabs)
├── 📄 agent.py          # AI logic and chat interface (GPT integration)
├── 📄 context.py        # Static knowledge base for RAG
├── 📄 styles.py         # CSS engine (responsive design & animations)
├── 📄 sidebar.py        # Navigation component
├── 📄 projects.py       # Project gallery module
└── 📄 requirements.txt  # Dependency management

⚙️ Key Engineering Highlights

Frontend-as-Code: Custom CSS/HTML injected via st.markdown, bypassing framework limitations to create a HUD-style UI.

Base64 Media Pipeline: Local encoding of video and audio assets to Base64, enabling zero-latency loading without external CDNs.

Responsive Engine: Advanced CSS media queries for mobile layouts, including custom menu positioning and touch-optimized interactions.

CI/CD: Automated deployment using Streamlit Cloud connected to GitHub.


🚀 Installation & Local Setup

To run the portfolio locally:

1. Clone the repository:
   git clone https://github.com/JesusSack/portfolio-cyberpunk.git
cd portfolio-cyberpunk


2. Install dependencies:
   pip install -r requirements.txt


3. Configure secrets (required for AI)

   Create the following file:
   # .streamlit/secrets.toml
      OPENAI_API_KEY = "           "

4. Run the application: 
   streamlit run main.py

📱 Mobile Optimization

The system includes dedicated mobile overrides:

Adaptive Layout: DOM structure reflows for vertical viewports.

Touch UX: Enlarged interactive elements for improved touch accuracy.

Visual Guidance: Directional indicator for the mobile menu to enhance usability.

📬 Contact

LinkedIn: Jesús Sack

Email: jesusmsack@hotmail.com


Built with ❤️ and 🐍 Python by Jesús Sack.





