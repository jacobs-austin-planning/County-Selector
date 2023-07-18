# County-Selector
Streamlit app script for selecting counties/US geographic boundaries. Has three current functions:

1. Manual Draw Option:
   Draw a line using the draw tools on the map and set a buffe r(in miles). All counties intersecting with the buffer will be selected. A table of all intersecting counties will be created. This table can be merged with a 
   .csv file if it includes a 5-digit FIPS code field. This merged dataframe can then be downloaded as a .csv.\

2. Road Network Option:
   A road network can be uploaded (lines, zipped .shp filed), which will apear on a map. Once a buffer distance is entered, the counties intersecting with the buffer will be selected and a dataframe of selected counties        will appear. This can further with merged with a .csv filed if it has a 5-digit FIPS code field.

3. Upload a shapefile
   A shapefile (point, line or polygon data) can be uploaded (in zipped format), which will appear on the map.

App Screenshot:

![US-County-Seletcor](https://github.com/jacobs-austin-planning/County-Selector/assets/137216501/de1cb97f-e08e-4789-bfa1-6f70fbe5a695)
