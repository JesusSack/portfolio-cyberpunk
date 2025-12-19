import streamlit as st
import os

def load_header_content():
   current_dir = os.path.dirname(os.path.abspath(__file__))
   file_path = os.path.join(current_dir, 'header.html')
    
   try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            clean_lines = [line.lstrip() for line in lines]
            return "".join(clean_lines)
            
   except FileNotFoundError:
        return "<h1 style='color:red'>ERROR: No se encuentra header.html</h1>"

def show_header():
    html_content = load_header_content()
    
    st.markdown(html_content, unsafe_allow_html=True)
    
    st.write("")