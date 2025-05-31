# Spatial
This repository contains the scripts to the exam project related to the Spatial Analytics course, which is an elective course at Aahurs University.

*Disclaimer:* For any data extraction from Google Maps, it is highly recommended to use the Google Places API

## License
This work is licensed under CC BY 4.0 

## Running the scripts ##

For the `Scraper.py` and `Rev_Geocoding.py` scripts it is necessary to install the packages from the requirements.txt, and for the `Exam.Rmd` the packages loaded at start of script need to be installed.

For the `Scraper.py` script, both Microsoft Edge and a webdriver (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH) with a compatible version is needed.  

The `Scraper.py` script needs an absolute path to the web driver and an absolute path to a unique user data directory. 

The `Scraper.py` script also needs a search word, which will be used to generate the search results that will be scraped.

## Analysis

The `Exam.Rmd` script creates and visualizes isochrones, and the intersections of different isochrones to highlight areas fulfilling multiple travel requirements. Examples of these visualizations can be seen in the `Out` folder.  
