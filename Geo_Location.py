# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:19:37 2017

Getting Geolocation from Given Place

@author: Hsemu
"""
from geolocation.main import GoogleMaps
import os

##location of saving the file
os.chdir('C:\\Users\Hsemu\Documents\Freelance\Geo_Location')

#Read the csv file
files = open("C:/Users/Hsemu/Documents/Freelance/Geo_Location/Geo_Location_2.csv","r")

file_list =  files.readlines()


##Check Quota if already reached
#address = "New York City Wall Street 12"
#location = google_maps.search(location=address) # sends search to Google Maps.
#print(location.all()) # returns all locations.

google_maps = GoogleMaps(api_key='AIzaSyB5tJPAsbJRMMm5s9Nqf91NbdTjsPQAHDE')


filename="Geo_Lat_lat_2.csv"
f=open(filename,"w")

headers="Address"+"|"+"Latitude"+"|"+"Longitude"+"\n"

f.write(headers)

for places in file_list:
      try:
          location = google_maps.search(location=places) # sends search to Google Maps.
          print(location.all()) # returns all locations.
          my_location = location.first() # returns only first location.
          f.write(places+"|"+str(my_location.lat)+"|"+str(my_location.lng)+"\n")
          print(my_location.lat)
          print(my_location.lng)
      except:
          pass

f.close()
