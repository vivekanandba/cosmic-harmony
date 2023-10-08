import streamlit as st

from components.graphs import plot_geo_with_size, plot_geo_with_size_and_year, plot_geo_with_size_and_year_log
from components.data_engg import load_data_and_clean_data   

st.set_page_config(page_title='Cosmic Harmony', page_icon='🌠')

df = load_data_and_clean_data()
st.markdown("<h1 style='text-align: center;'>Please participate in checking out the meteorites!</h1>", unsafe_allow_html=True)
st.divider()
st.markdown("<h2 style='text-align: center;'>Meteorites with size animated over time</h2>", unsafe_allow_html=True)
st.plotly_chart(plot_geo_with_size_and_year(df, projection='natural earth'))
st.divider()
st.markdown("<h2 style='text-align: center;'>Meteorites with size across time</h2>", unsafe_allow_html=True)
st.plotly_chart(plot_geo_with_size(df, projection='natural earth'))
st.divider()
st.markdown("<h2 style='text-align: center;'>Meteorite Landings size of meteorite vs year</h2>", unsafe_allow_html=True)
st.plotly_chart(plot_geo_with_size_and_year_log(df))
st.divider()
st.markdown("<h2 style='text-align: center;'>Data Tabulation</h2>", unsafe_allow_html=True)
df.drop(['id','class','year'], axis=1, inplace=True)
df.rename(columns={'name':'Name','mass': 'Mass (kg)', 'fall':'Fall', 'year':'Year', 'latitude':'Latitude', 'longitude': 'Longitude', 'class_cat':'Class'}, inplace=True)
# sort dataframe by index
df.reset_index(inplace=True)
df.drop(['index'], axis=1, inplace=True)
df.sort_index(inplace=True)
st.dataframe(df)
st.divider()