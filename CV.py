import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


st.write("Voici mon CV")
image = Image.open('C:/Users/yfour/OneDrive/Documents/papier/CV.jpg')
st.image(image, caption="Mon CV", width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)