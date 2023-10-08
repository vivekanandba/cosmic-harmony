# %%
import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")
# %%
len(df)
# %%
# draw the latitude longitude on to a map
df.dtypes
# %%
# check which columns have missing values
df.isnull().sum()

# %%
# drop rows with missing values
df = df.dropna()
# %%
len(df)
# %%
# plot the latitude longitude using plotly express

import plotly.express as px

fig = px.scatter_geo(df, lat='reclat', lon='reclong')
fig.show()

# %%
import folium

# create a map centered on the mean latitude and longitude values
m = folium.Map(location=[df['reclat'].mean(), df['reclong'].mean()], zoom_start=2)

# add a marker for each row in the dataframe
for index, row in df.iterrows():
    folium.Marker(location=[row['reclat'], row['reclong']]).add_to(m)

# display the map
m
# %%
