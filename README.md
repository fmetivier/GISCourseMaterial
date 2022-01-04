# GIS Course: sample scripts

* [Introduction](##introduction)
* [Requirements and Installation](##requirements-and-installation)
* [Content](##content-of-the-src-folder)

  * [Folium](###folium-directory)
  * [Python-SQL](###python-mysql-directory)
  * [Maps](##map-directory)
* [SQL](###sql-directory)



## Introduction

The python files enclosed include the scripts discussed in the following undergraduate Course:

*Bases de données et cartographie en Sciences de la terre avec MariaDB (MySQL) et Python L3-Terre & Environnement*, given at Institut de Physique du Globe de Paris by François Métivier

The course (only in French for now) can be freely downloaded on [HAL] as a pdf (https://cel.archives-ouvertes.fr/cel-01877606v3).

Its present version concentrates on the cartopy library that has become the *de facto* standard for maps in python. Yet for those who still use basemap  scripts are given for most of the programs and previous versions of the course are also available on HAL.

I try to keep and up-to-date versions of the course and files for students as I add new scripts.


## Requirements and Installation

For the scripts to work you will need python 3 installed (some of the scripts also work in python 2.7 but some changes like for example the zip function do limit the portability). You will also need a MariaDB or MySQL server with administrator (at least some) priviledges to perform the scripts that connect to databases and perform SQL queries.

The python libraries needed to run all the scripts include
* basemap or cartopy for maps
* folium for webmaps
* matplotlib, numpy and scipy for figures and numerics
* pyshp, pyproj, pyepsg, shapely, pandas, geopandas  for gis and data processing (pandas and geopandas are not mandatory though)
* python-gdal and gdal
* python-mysql and/or sqlalchemy for connections to database servers.

if you use python environments like anaconda or use the library managers of linux, the dependencies should be resolved by themselves upon installation of the main libraries (namely cartopy, mysqldb, sqlalchemy and pandas/geopandas).

The scripts have been tested on computers running under  linux (Debian), windows, and various versions of MacOS.

The links inside the scripts are referenced with regard to the script so
you need to reconstruct the working directory. Because Github is not a data repository you have to proceed in two steps

  * Clone the root directory wherever you want.

  * Then download the datasets used in the scripts from http://morpho.ipgp.fr/metivier/public/include/Data/GISCoursMaterialData.zip
   and place them in the Data folder of the root directory so that the overall architecture is the following

  ```
  ./GISCourseMaterial:
    ./Data
      ./folium
        ...
      ./map
        ...
      ./sql
        ...
    ./src
      ./folium
      ./map
      ./python-mysql   
  ```

## Content of the src folder

Each directory in the src folder corresponds to certain types  python scripts discussed in the different chapters of the course.

With the exception of the sql directory, each directory is organised in three directories

The src directory contains all the source codes, the include directory contains all the data needed to execute the scripts, the figures directory shows some results.

### folium directory

Scripts to produce interactive webmaps (Part II chapter 14) using the folium library.

| Script| Purpose |
|----|---|
|<a target="_blank" href="./folium/src/f_1.py">f_1.py</a>| Location of IPGP's sites as markers on an OSM map|
|<a target="_blank" href="./folium/src/f_2.py">f_2.py </a>| Exemple of maps made of wms server layers |
|<a target="_blank" href="./folium/src/f_3.py">f_3.py </a>| Earthquakes of the last seven days plotted on top of two wms layers and the OSM basemap|
|<a target="_blank" href="./folium/src/f_4.py">f_4.py </a>| Cluster Markers to plot places visited by students |
|<a target="_blank" href="./folium/src/f_5.py">f_5.py</a>| Transform GeoJson polygons and add information Popups |
|<a target="_blank" href="./folium/src/f_6.py">f_6.py</a> | Plot Choropleth from a shapefile |
|<a target="_blank" href="./folium/src/f_7.py">f_7.py</a>| Plot Northern atlantic Hurricanes trajectories |
|<a target="_blank" href="./folium/src/f_8.py">f_8.py</a> | Plot Groundwater piezometric map of the Landes sand aquifer on top of OSM basemap |
|<a target="_blank" href="./folium/src/ShapeTransform.py">ShapeTransform.py </a>| library to tranform a  shapefile geometry into a geojson dic and a pandas dataframe |




### python-mysql directory

These scripts are meant to show how pyton can interact with sql databases (Part I chapters 5-6 and appendix).

Each script makes use of a text file called "identifiers.txt" where the login and password are stored on two lines

```
  yourlogin
  yourpassword
```
The file is then read according to

```python
#get your connection identifiers
f=open('./identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')
```
The purpose here is to be able to share scripts without sharing login information !


| Script| Purpose |
|----|---|
|<a target="_blank" href="./python-mysql/src/openDB.py">openDB.py</a> | Class OpenDB library: simple wrapper to connect and execute SQL queries (DDL and DML). Saves time :=) |
|<a target="_blank" href="./python-mysql/src/pm_1.py">pm_1.py</a> | Query and plot the number of registered students|
|<a target="_blank" href="./python-mysql/src/pm_2.py">pm_2.py</a>, <a target="_blank" href="./python-mysql/src/pm_4.py">pm4_py</a>, <a target="_blank" href="./python-mysql/src/pm_4p.py">pm_4p.py</a> | Query the imetos database and plot the daily rainfall. The three scripts use three different ways to query the database |
|<a target="_blank" href="./python-mysql/src/pm_3.py">pm_3.py</a> & <a target="_blank" href="./python-mysql/src/pm_3_1.py">pm_3_1.py</a>| sample Data Definition Language (DDL) scripts|
|<a target="_blank" href="./python-mysql/src/pm_5.py">pm_5.py</a> | Plot of the hourly temperatures  averaged over july,August and september |
|<a target="_blank" href="./python-mysql/src/pm_6.py">pm_6.py</a> | Plot the histogram of wind directions as a polar plot.|
|<a target="_blank" href="./python-mysql/src/pm_7.py">pm_7.py</a>, <a target="_blank" href="./python-mysql/src/pm_7_2.py">pm_7_2.py</a> & <a target="_blank" href="./python-mysql/src/pm_8.py">pm_8.py</a>| use pandas to connect to a mysql/MariaDB server |
|<a target="_blank" href="./python-mysql/src/pm_9.py">pm_9.py </a>| Use pandas to write data to an SQL server |
| <a target="_blank" href="./python-mysql/src/sqla_1.py">sqla_1.py </a>| Ways to connect to a mysql/mariadb server using sqlalchemy and different connectors |
|<a target="_blank" href="./python-mysql/src/sqljoins.py">sqljoins.py </a>| Plot of different types of SQL joins |

Several scripts are also given  to help students with graphics before going into maps

| Script| Purpose |
|----|---|
|<a target="_blank" href="./python-mysql/src/pm_A1.py">pm_A1.py</a> | Plot xcos(x) |
|<a target="_blank" href="./python-mysql/src/pm_A2.py">pm_A2.py</a> | Plot Solution of a steady 1D flow using Dupuit approximation over a length L for different values of hydraulic conductivity K Boundary conditions are a flux  Q at 0 and zero depth y at 1.|
|<a target="_blank" href="./python-mysql/src/pm_A3.py">pm_A3.py</a> & <a target="_blank" href="./python-mysql/src/pm_A3_1.py">pm_A3_1.py</a> |Using axes in matplotlib pyplot figures |
|<a target="_blank" href="./python-mysql/src/pm_A4.py">pm_A4.py</a> | Drawing circles, using patches and collections |
|<a target="_blank" href="./python-mysql/src/pm_A5.py">pm_A5.py </a>| Different ways to build a legend |
|<a target="_blank" href="./python-mysql/src/replace_X.py">replace_X.py</a> | Replacing ticks|


### map directory

Scripts and datasets used to show how python can be used to draw nice maps (Parti II chapters 7-13). Scripts are presented with python main cartographic libraries

* basemap (bm_xx.py)
* cartopy (cm_xx.py)

| Scripts | Description |
|----|---|
|cm_1.py |  Simple map taken from cartopy tutorial |
|cm_1_2.py & cm_1_3 | keywords : projection vs transform |
|cm_2.py | Change projection, add gridlines |
|cm_4.py & cm_4_1.py| Add labels |
|cm_5.py | Draw points and great circle |
|cm_5_backgrounds.py, cm_5_backgrounds_vec.py & cm_5_background_img.py | Backgrounds from NaturalEarth and images |
|cm_5_EQ.py | Earthquake map |
|cm_5_SVZ.py | Magnetic map |
|bm_6.py | Read shapefiles using the osgeo library |
|cm_7.py | Read shapefile with cartopy |
|cm_8.py | Fill polygns with colours |
|bm_9.py | Convert shapefile using geopandas (not specific to bm)|
|bm_10.py | Write data to a shapefile (not specific to bm) |
|bm_11.py | Get information from a georefenced image (not specific to bm) |
|cm_12.py |Plot a georeferenced jpeg image of Aquitaine with Bordeaux |
|cm_12_2.py | Plot a georeferenced DEM using merging and cropping |
|bm_13.py | Open Raster bands from a Geotiff Landsat 5 image; Extract and plot the histograms |
|cm_14.py & bm_14.py| Stretch, merge and reproject GeoTiff images. The case of the Bayanbulak grassland in Tianshan. |
|cm_15.py, cm_15bis.py, bm_15.py & bm_15bis.py| Plot a choropleth of the french departements together with some query over the Parcours database |
|cm_16.py & bm_16.py |Draw equipotential (isopieze map) lines of the Plio-quaternary aquifer on top of a Landast ETM view of the Lakes of Landes south of Arcachon. The ETM image comes from the earthdata web service |
|bm_18.py |Create the DEPARTEMENT Table  and populate it using the GEOFLA shapefile and osgeo library |


## sql databases

The databases  used throughout the course but are discussed in more detail in Part I chapters 1-4). They are not included in the github repository but because they are needed some explanation follows. I have chosen MariaDB / MySQL  for several reason.

* First of all MariaDB is a true database management server so it is a very good introduction to these systems for students compared to for example sqlite3 which is simpler but does not include many of the DDL features of a server.

* Second the choice of MariaDB over postgresql is related to simplicity. Although postgresql is clearly better for the management and query of geometries, it is much more complex then mysql and mariadb.

* Eventually MariaDB (or more precisely in this case MySQL) is probably the widest database server in use today due to LAMP web servers. Thus some working  knowledge  of MariaDB (MySQL) can be of practical use for students in a much browder context than just GIS programming.

the sql folder has no subfolders and contains dumps of the databases. Provided you have the necessary privileges, the dumps  can be uploaded to a MariaDB or MySQL server through  the classic command

```SQL
    mysql -u your_login -p your_pass < database_name.sql
```

| Base | Description |
|----|---|
|Charts.sql | French charts (Top 50) of single albums since the beginning of Top 50. Last year: |
|GEMS.sql | GEMS database of world rivers from the UNEP program |
|hurricanes.sql| Database of Atlantic Ocean hurricanes maintained by NOAA, last year: |
|Parcelle.sql | Sample meteorological data aquired with an imetos weather station |
|Parcours.sql | database of student places |
|Quake4plus_corr.csv | Earthquakes of M >= 4 from 2010-09-07 to 2018-09-08 extracted from USGS datacenter|
|tata.csv | Fake datafile to play with |
