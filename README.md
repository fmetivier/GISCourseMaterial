# GIS Course Material

## Introduction

The files enclosed include the datasets and scripts discussed in the follwing undergraduate Course:

*Bases de données et cartographie en Sciences de la terre avec MariaDB (MySQL) et Python L3-Terre & Environnement*, given at Institut de Physique du Globe de Paris by François Métivier
The course can be downloaded on [HAL](https://cel.archives-ouvertes.fr/cel-01877606v1)

## Requirements

For the scripts to work you will need
* python 3 installed (some of the scripts also work in python 2.7 but some changes like for the zip function do limit the portability)
* MariaDB or MySQL server with administrator (at least some) priviledges.

python libraries needed to run all the scripts include
* basemap and cartopy for maps
* folium for webmaps
* matplotlib, numpy and scipy for figures and numerics
* pyshp, pyproj, shapely, pandas, geopandas  for gis and data processing
* python-gdal and gdal for gis also
* python-mysql, sqlalchemy for connections to database servers

The scripts have been tested on PCs using windows, and linux (Debian) and Macs.

## Content

each directory corresponds to certain types of datasets and python scripts discussed in the different chapters of the course

### folium

Scripts to produce interactive webmaps (Part II chapter 14) using the folium library.

### SQL

Series of database dump that can be uploaded to a MariaDB or MySQL server  the classic command

    mysql -u your_login -p your_pass < database_name.sql

The databases are used throughout the course but are discussed in more detail in Part I chapters 1-4)

### python-mysql

scripts used to show how pyton can interact with sql databases (Part I chapters 5-6 and appendix)

### map

Scripts and datasets used to show how python can be used to draw nice maps (Parti II chapters 7-13). scripts are presented with python main cartographic libraries
* basemap (bm_xx.py)
* cartopy (cm_xx.py)
