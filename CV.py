import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

path = "C:/Users/yfour/OneDrive/Documents/Mon_CV_Streamlit"
img_cv = path + "\image\CV.pdf"
img_profil = path + "\image\Profil.pdf"

st.write("Voici mon CV")
image = Image.open(img_cv)
st.image(image, caption="Mon CV", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
image = Image.open(img_profil)
st.image(image, caption="Mon CV", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
