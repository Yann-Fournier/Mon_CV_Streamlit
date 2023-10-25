#import
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Variable
img_profil = Image.open("assets/Profil.png")
html_file =  "html/main.html"
css_file =  "style/main.css"
js_file =  "js/main.js"

# Liaison du css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(js_file) as f:
    st.markdown("<script>{}</script>".format(f.read()), unsafe_allow_html=True)

    
# Début du CV
st.write("---") # Séparation en markdown
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
with open(html_file) as f:
    st.markdown("<html>{}</html>".format(f.read()), unsafe_allow_html=True)
    
#     st.title(NAME)
#     st.write(DESCRIPTION)

#     st.write("📫", EMAIL)


