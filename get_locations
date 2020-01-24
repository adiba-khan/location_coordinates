from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import json

#load list of hospitals to locate and characters to be replaced
hospitals = pd.read_csv("hospitals.csv")
replacements = pd.read_csv("character_rpls.csv")

#remove dashes, THEN replace spaces with "+" for search
hospitals["Hospital Name"] = hospitals['Hospital Name'].str.replace("-", "").str.replace("–","").str.replace(" ","")

#replace non-ascii characters with ascii characters
for i in range(len(replacements)):
	hospitals["Hospital Name"] = hospitals['Hospital Name'].str.replace(replacements["non"][i],replacements["ascii"][i])

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

    print(text['results'][0]["geometry"]["location"])
    print(list[j])

    #if results are empty i want to list the name of hospital and locate it manually?

    #latitudes.append(text['results'][0]["geometry"]['location']["lat"])
    #longitudes.append(text['results'][0]["geometry"]['location']["lng"])

"""lat = pd.Series(latitudes)
lng = pd.Series(longitudes)

hospitals['latitudes'] = lat.values
hospitals['longitudes'] = lng.values

lat.to_csv("latitudes.csv")
lng.to_csv("longitudes.csv")
"""
#hospitals.to_csv("lat_lng_hospitals.csv")
