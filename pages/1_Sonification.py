import streamlit as st

st.set_page_config(page_title='Cosmic Harmony', page_icon='🌠')

st.title("A Sonification of Meteorite Showers")
# st.header("Cadence of the Meteorites ")
st.divider()
# st.header("Experience the Cadence of the Meteorites")
st.markdown("### We created this immersive experience, so it`s accessible to both, those with vision, and those who perceive beyond sight.")
st.divider()
st.video("data/intro.mp4")
st.divider()
# st.markdown("#### Chronicles of the Meteorites")

st.markdown("""
Meteorite discoveries and impacts have been a part of human history for millennia. 

Some meteorites have had significant impacts on both science and culture.

Explore this interactive 3D map of the twenty largest meteorites to learn the real-life stories behind them.

""")
st.divider()
# st.video('output/videos/meteor_impacts-fps-10.mp4')
st.video('data/jazz-ensemble-black-bar.mp4')
st.divider()