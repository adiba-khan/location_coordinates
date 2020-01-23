from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import json

hospitals = pd.read_csv("hospital.csv")

list = []
for i in range(len(hospitals)):
    list.append(hospitals["Name"][i])

# use the google map api

for j in range(len(list)):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={list[j]}&key=AIzaSyA-w4Ggq4Pw6dEesydVgsxSmgAX9aOB-AQ'
    jsonurl = urlopen(url)

    text = json.loads(jsonurl.read())

    print ( text['results'][0]["formatted_address"])
    print ( text['results'][0]["geometry"]['location']["lat"])
    print ( text['results'][0]["geometry"]['location']["lng"])
