import streamlit as st
import os

# TEST SIMPLE: Si esto no funciona, es tu navegador o el formato del video
video_file = open("background.mp4", "rb").read()
st.video(video_file)