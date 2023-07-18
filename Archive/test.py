# Geospatial Querying Tool
# County Shapefile: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html


#----
# Required Packages
#----
import folium
import streamlit as st
from streamlit_folium import st_folium
from folium.plugins import Draw
import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString
import geojson
#----

#----
# Page Setup

#----

# Functions

@st.cache_data(experimental_allow_widgets=True)
def main():
    st.title("US County Selector")

    m = create_map()

    map = st_folium(m,
    width=1800,  
    height=500)
    return map

def map_data():
    counties_dat = "c:/Users/aroras4/Desktop/Shapefiles/cb_2018_us_county_20m.shp"
    counties_data = gpd.read_file(counties_dat)
    return counties_data

def create_map():
    style_func = lambda x: {'fillColor': 'grey', 'color': "#000000", 'weight': 0.5, 'fillOpacity': 0.6}
    m = folium.Map(location=[38, -80.5], zoom_start=4, control_scale=True)
    counties_data=map_data()
    folium.GeoJson(counties_data, style_function=style_func, 
               tooltip=folium.features.GeoJsonTooltip(fields=['NAME', 'GEOID'], aliases=['County Name: ', 'FIPS: '])).add_to(m)
    draw = Draw()
    draw.add_to(m)
    return m

def make_ls():
    # Calling from data stored in st_folium
    m = main()
    if "last_active_drawing" in m is not None and "geometry" in m["last_active_drawing"] is not None and \
            "coordinates" in m["last_active_drawing"]["geometry"] is not None:
        linestring = LineString(m["last_active_drawing"]["geometry"]["coordinates"])
    else:
        linestring = LineString()

    global map
    return linestring
    
def add_intersecting_polygons_to_map():
    linestring = make_ls()
    counties_data = map_data()
    buffered_line = linestring.buffer(2)
    intersecting_polygons = counties_data[counties_data.geometry.intersects(buffered_line)]

    intersect = folium.GeoJson(intersecting_polygons,
                               tooltip=folium.features.GeoJsonTooltip(fields=['NAME', 'GEOID'], aliases=['Selected County Name: ', 'FIPS: ']))
    buffer = folium.GeoJson(buffered_line)
    st.session_state["markers"].append(buffer) #Send data to session state
    st.session_state["markers"].append(intersect)

    global map
    return intersecting_polygons


#----

if __name__ == "__main__":

    # Page Setup
    st.set_page_config(
    layout="wide",
    page_title="County-Selector"
)

    if 'markers' not in st.session_state:
        st.session_state["markers"] = []

    fg = folium.FeatureGroup(name="Markers")
    for marker in st.session_state["markers"]:
        fg.add_child(marker)

    main()

add_intersecting_polygons_to_map()
