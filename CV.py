#import
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Variable
img_profil = Image.open("assets/Profil.png")

# Liaison du css
with open("style/main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Début du CV
st.write("---") # Séparation en markdown

# Colonnes de la première partie
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(img_profil, width=302)

with col2:
    st.title("Yann Fournier")
    st.write("29/11/2004 (19 ans)")
    st.write("Etudiant en informatique à Paris Ynov Campus.")
    with open("assets/CV.pdf", "rb") as file:
        st.download_button(
        label=" 📄 Download Resume",
        data=file,
        file_name="CV-Yann-Fournier.pdf",
        mime="application/octet-stream",
        )
    st.write("📱", "(+33) 06 95 71 31 00")
    st.write("📧", "ya.fourni@icloud.com")
    st.write("[- Mon Github](https://github.com/Yann-Fournier)")
    st.write("[- Mon Linkedin](https://www.linkedin.com/in/yann-fournier-243453296/)")

st.write("---") # Séparation en markdown

# ajout fichier html sur mes skills
with open("html/main.html") as f:
    st.markdown("<html>{}</html>".format(f.read()), unsafe_allow_html=True)

st.write("---") # Séparation en markdown


