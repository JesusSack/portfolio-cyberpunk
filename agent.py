import streamlit as st
from openai import OpenAI
from context import SYSTEM_PROMPT

def show_chatbot():
    # ESTILOS CSS
    st.markdown("""
    <style>
        /* Contenedor del input fijo abajo */
        .stChatInputContainer {
            padding-bottom: 20px;
        }
        
        /* Burbujas de chat */
        .stChatMessage {
            background-color: rgba(10, 10, 10, 0.8) !important;
            border: 1px solid #333;
            border-radius: 5px;
        }
        
        /* Texto del usuario y del asistente */
        div[data-testid="stChatMessageContent"] {
            color: #e0e0e0;
            font-family: 'Roboto Mono', monospace;
            font-size: 0.95rem;
        }

        /* Avatar del asistente */
        .stChatMessage .stChatMessageAvatar {
            background-color: #00ffff;
            color: #000;
        }
    </style>
    """, unsafe_allow_html=True)

    #    Título actualizado
    st.markdown("### 🤖 AI Agent")
    st.caption("Ask me about Jesús's skills, experience, or this project's architecture.")

    # 1. VERIFICAR API KEY
    if "OPENAI_API_KEY" not in st.secrets:
        st.error("⚠️ SYSTEM ERROR: OpenAI API Key not found in secrets.")
        st.info("Please configure `.streamlit/secrets.toml` to enable the AI Agent.")
        return

    # 2. INICIALIZAR CLIENTE OPENAI
    if "openai_client" not in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # 3. INICIALIZAR HISTORIAL DE CHAT
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": "System Online. How can I assist you regarding Jesús's profile?"}
        ]

    # 4. MOSTRAR HISTORIAL (Excluyendo el mensaje del sistema)
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # 5. CAPTURAR INPUT DEL USUARIO
    if prompt := st.chat_input("Initialize query..."):
        # A) Mostrar mensaje usuario
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # B) Generar respuesta asistente
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Llamada a la API con Streaming
                stream = st.session_state.openai_client.chat.completions.create(
                    model="gpt-3.5-turbo", # "gpt-4o"
                    messages=st.session_state.messages,
                    stream=True,
                )
                
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # C) Guardar en historial
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"⚠️ Connection Error: {e}")