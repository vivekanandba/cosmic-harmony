import streamlit as st
from PIL import Image
from pathlib import Path

image_dir = Path('images')

st.set_page_config(page_title='Cosmic Harmony', page_icon='🌠')

st.title("A Sonification of Meteorite Showers")
st.header("Cadence of the Meteorites ")
st.text("`Meteorites might be the metronome that sets the cadence of biological evolution on Earth`")

#insert image

image = Image.open(image_dir / 'poster.jpeg')
st.image(image, caption='Cosmic Harmony', use_column_width=True)
