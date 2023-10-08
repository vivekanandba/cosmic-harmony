import streamlit as st
from PIL import Image
from pathlib import Path

from components.graphs import plot_geo_with_size, plot_geo_with_size_and_year, plot_geo_with_size_and_year_log
from components.data_engg import load_data_and_clean_data 

image_dir = Path('images')

st.set_page_config(page_title='Cosmic Harmony', page_icon='🌠')

st.markdown("# Join us on a unique journey, \n # a symphony of the cosmos.")
st.divider()
# st.header("Cadence of the Meteorites ")
# st.text("`Meteorites might be the metronome that sets the cadence of biological evolution on Earth`")

st.text("""
Let’s follow along meteorites
—yes, those celestial wanderers—
as they make their appearances into our world.
 
In the vast cosmic tapestry, meteorites are but tiny threads,
remnants of our primordial solar neighborhood.
 
Like cosmic messengers, they travel vast distances
to bring whispers of our distant past.
 
We'll take you on a sonic voyage through time,
from more than five hundred years ago 
to the present day.
""")
  
df = load_data_and_clean_data()

st.plotly_chart(plot_geo_with_size(df, projection='orthographic'))