from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import json
import re
import unicodedata

#load list of hospitals to locate
hospitals = pd.read_csv("hospitals.csv")

#remove dashes, multiple white spaces

hospital_names = []
replace_non_ascii = lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8')
for name in hospitals["Hospital Name"]:
    name = name.replace(chr(45), "").replace(chr(8211),"")
    hospital_names.append(replace_non_ascii(re.sub(r'\s\s+', ' ', name).replace(" ","+")))

#replace spaces with "+" for search
hospitals["Hospital"] = hospital_names
hospitals["Country"] = hospitals["Country"].str.replace(" ","+")

#create list of cleaned up hospital names to search in api
list = []
for i in range(len(hospitals)):
    list.append(f"{hospitals['Hospital Name'][i]}+{hospitals['Country'][i]}")

# use the google map api

latitudes = []
longitudes = []

for j in range(len(list)):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={list[j]}&key=%YOUR GOOGLE KEY'
    jsonurl = urlopen(url)

    text = json.loads(jsonurl.read())

    latitudes.append(text['results'][0]["geometry"]["location"]["lat"])
    longitudes.append(text['results'][0]["geometry"]['location']["lng"])

#add latitude and longitude columns and remove modified country and hospital columns
lat = pd.Series(latitudes)
lng = pd.Series(longitudes)

hospitals['latitudes'] = lat.values
hospitals['longitudes'] = lng.values

hospitals = hospitals.drop({"Country", "Hospital"}, axis=1)

print(hospitals)
#save to csv
hospitals.to_csv("lat_lng_hospitals.csv")
