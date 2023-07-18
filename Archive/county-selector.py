# Geospatial Querying Tool
# County Shapefile: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html


#----
# Required Packages
#----
import folium
import streamlit as st
from streamlit_folium import  st_folium
from folium.plugins import Draw
import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString
#import geojson
#----

#----
# Page Setup

st.set_page_config(
    layout="wide",
    page_title="County-Selector"
)

st.title("US County Selector")

st.write("This tool displays US County Boundaries from US Census Bureau's Cartographic Boundary Files. Draw a line to create a buffer (in miles) to select and display the intersecting counties. Additionally, you can add a road network file (.shp) from the sidebar and enter a buffer distance to highlight the intersecting counties. The resulting table can be converted into a .csv file. To add your own data to the selected counties, upload a .csv file with a FIPS code field in the sidebar.")

#---

#----
# Initializing session state for streamlit

if 'lines' not in st.session_state:
    st.session_state["lines"] = []

fg = folium.FeatureGroup(name="Lines")
for line in st.session_state["lines"]:
    fg.add_child(line)

# Basemap with US Counties

@st.cache_data
def base_map(url):
    counties_data = gpd.read_file(url)
    counties_data = counties_data.drop(['COUNTYNS', 'AFFGEOID', 'LSAD', 'ALAND', 'AWATER'], axis=1)
    return counties_data

counties_data = base_map("c:/Users/aroras4/Desktop/Shapefiles/cb_2018_us_county_20m.shp")


m = folium.Map(location=[38, -80.5], zoom_start=4, control_scale=True)
style_func = lambda x: {'fillColor': 'grey', 'color': '#000000', 'weight': 0.5, 'fillOpacity': 0.6}
folium.GeoJson(counties_data, style_function=style_func, tooltip=folium.features.GeoJsonTooltip(fields=['NAME', 'GEOID'], aliases=['County Name: ', 'FIPS: '])).add_to(m)
    
draw = Draw()
draw.add_to(m)

map = st_folium(m,
feature_group_to_add=fg,
width=1800,  
height=500)

base_map()



