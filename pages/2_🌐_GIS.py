import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium import features
from data import *


st.set_page_config(
    page_title="GIS",
    page_icon="🌐",
    initial_sidebar_state="collapsed",
    layout="wide"
)

st.title("GIS Data")


jsonFile = "usState.geojson"

m = folium.Map(location=[40, -96], name="Light Map", zoom_start=5, tiles="openstreetmap")
v = folium.Map(location=[40, -96], name="Light Map", zoom_start=5, tiles="openstreetmap")

# Cases
folium.Choropleth(
    geo_data=jsonFile,
    name="choropleth",
    data=state_total,
    columns=["Location", "Cases"],
    key_on="feature.properties.ste_name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.1,
    legend_name="Cases In US"
).add_to(m)

folium.features.GeoJson('usState.geojson', name="States", popup=folium.features.GeoJsonPopup(fields=["ste_name"])).add_to(m)


# Vaccines
folium.Choropleth(
    geo_data=jsonFile,
    name="choropleth",
    data=state_vac,
    columns=["Reporting Jurisdictions", "Total"],
    key_on="feature.properties.ste_name",
    fill_color="YlOrBr",
    fill_opacity=0.7,
    line_opacity=0.1,
    legend_name="Vaccines Adminstered in the US"
).add_to(v)

folium.features.GeoJson('usState.geojson', name="States", popup=folium.features.GeoJsonPopup(fields=["ste_name"])).add_to(v)


folium_static(m, width=1600, height=950)

st.write("Some text")

folium_static(v, width=1600, height=950)
