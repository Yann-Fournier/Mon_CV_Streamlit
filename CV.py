import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.write("Voici mon CV")
image = Image.open('./image/CV.jpg')
st.image(image, caption="Mon CV", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
image2 = Image.open("image/Profil.png")
st.image(image2, caption="Mon CV", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
