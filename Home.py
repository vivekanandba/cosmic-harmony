import streamlit as st
from PIL import Image
from pathlib import Path

from components.graphs import plot_geo_with_size, plot_geo_with_size_and_year, plot_geo_with_size_and_year_log
from components.data_engg import load_data_and_clean_data 

image_dir = Path('images')

st.set_page_config(page_title='Cosmic Harmony', page_icon='🌠')

st.markdown("<h1 style='text-align: center;'>Join us on a unique journey, a symphony of the cosmos.</h1>", unsafe_allow_html=True)
st.divider()

st.markdown(
    """
> <div style='text-align: center;'>
>     <p>Let’s follow along meteorites
>     —yes, those celestial wanderers—
>     as they make their appearances into our world.</p>
>     <p>In the vast cosmic tapestry, meteorites are but tiny threads,
>     remnants of our primordial solar neighborhood.</p>
>     <p>Like cosmic messengers, they travel vast distances
>     to bring whispers of our distant past.</p>
>     <p>We'll take you on a sonic voyage through time,
>     from more than five hundred years ago 
>     to the present day.</p>
> </div>
    """,
    unsafe_allow_html=True
)
  
st.video("data/intro.mp4")
st.divider()