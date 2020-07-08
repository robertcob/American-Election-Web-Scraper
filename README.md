# American-Election-Web-Scraper
Project begins by using selenium (python api testing/web-scraping module) to scrape relevant polling data information on every state and project into a text
files where the information is organized (ie dates formatted etc)

![text file snippet](images/edited_Data.PNG?raw=true "Sample Text File")

Using mongodb python API "Pymongo" all infomation that is suitable is added to a database without duplicates.
Read Operations are performed to create average Trump/Biden polling data values for all states that have information available.
Thes figures are then projected as a dictionary and added into the dbf file which is edited using geopandas/pandas and pythons csv module.

Using matplotlib, geopandas and numpy the mapping data is combined with the election data gathered to create a color coded map based on aggregated percentage polling values.
  

![electoral_Map](images/electoral_Map.PNG?raw=true "Electoral Map")

The map has a series of colors
* The light green indicates states that do not have sufficient polling data to be projected.
* Anything blue are states leaning democratic
* Anything red are states leaning republican
* Anything grey is a tie.
* This map is of polling data from June 20th

All of these polling values are subject to change over time.

I found the initial map data at this site..
[Initial Election data](https://www.arcgis.com/home/item.html?id=f7f805eb65eb4ab787a0a3e1116ca7e5)

This is what the map looks like initailly projected

![ Initial Electoral Map](images/inital_MapPNG.PNG?raw=true "Electoral Map")

I then used various algorithms and projection methods that are found in Arc Gis software to change this map to better suit my needs

![ Edited Electoral Map](images/edited_MapPNG.PNG?raw=true "Electoral Map")

Color coding and resizing of the projection was completed with matplotlib.

List of all resources used
* Selenium
* Matplotlib
* Numpy
* GeoPandas, Pandas, csv edit etc
* Arc Gis
* Mongodb/Pymongo


