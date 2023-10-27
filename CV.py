#import
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Liaison du css
with open("style/main.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Début du CV
st.write("---") # Séparation en markdown

# Colonnes de la première partie
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("assets/Profil.png", width=302)

with col2:
    st.title("Yann Fournier")
    st.write("29/11/2004 (19 ans)")
    st.write("Etudiant en informatique à Paris Ynov Campus.")
    with open("assets/CV.pdf", "rb") as file:
        st.download_button(
        label=" 📄 Télécharger mon CV",
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

st.subheader("Expériences étudiantes")


st.write("---") # Séparation en markdown
st.subheader("Expériences professionelles")

st.write(" Bio life / vendeur (Octobre 2021 – Avril 2022)")
st.write("""
    - Mise en étalage des fruits et légumes sur le marché de la Garenne 
    Colombes, 
    - Déchargement et chargement de la marchandise, 
    - Accueille et vente auprès des clients 
    - Gestion de la caisse 
""")

st.write("Aviva Assurances / stage d’observation de 3e  (Décembre 2019)")
st.write("""
    - Compréhension de l’organisation de l’entreprise 
    - Interview des directeurs 
    - Rédaction d’un rapport de stage
""")

st.write("Collège Les Vallées / concours projet fusée (2017, 2018, 2019)")
st.write("""
    - Construction en équipe d’une fusée selon certains critères et en compétition 
    face à d’autres équipes.
""")

st.write("---") # Séparation en markdown

st.subheader("Formations")

st.write("""
    - 2023-2024 : Deuxième année en école d’ingénieure en informatique à Paris Ynov Campus.
    - 2022-2023 : Première année en école d’ingénieure en informatique  à Paris Ynov Campus.
    - 2022 : Obtention du Baccalauréat avec mention Très Bien.
    - 2021-2022 : Terminale générale au lycée Paul Lapie avec spécialité 
    Mathématiques, Science du Numérique et de l'Informatique (NSI) et option Maths Expert. 
    - 2020-2021 : 1er générale au lycée Paul Lapie avec option Maths, 
    Physique chimie et Science du Numérique et de l'Informatique (NSI). 
    - 2019 : Obtention du Brevet des Collèges - Mention TB
""")

st.write("---") # Séparation en markdown

# Colonnes de la première partie
colonne3, colonne4 = st.columns(2, gap="small")

with colonne3:
    st.subheader("Centres d'interêt")

    st.write("""
        - Sports:  🏐Volley-ball, 🤸Callisthénie 
        - Jeux vidéos: Apex, 🚗Rocket League
        - Lecture: Livre sur la 📈finance, sur la 🪐science et des mangas
    """)

with colonne4:
    st.subheader("Points Forts")

    st.write("""
        - Ponctuel, 
        - Organisé, 
        - Sociable et souriant, 
        - Appliqué dans mon travail 
        - Esprit d’équipe 
    """)
