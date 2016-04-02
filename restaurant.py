import requests
import urllib2
import json
import yaml
import re
from json import load, dumps
lat="12.8446784"
lon="77.6610528"

def getDist(originLat,originLon, destLat, destLon):
    if destLat=="0.0000000000":
        return "NA"
    api_key="AIzaSyDCxrDO4MC2N4H30q7iTfge2hGQLe14kuE"
    base_url="https://maps.googleapis.com/maps/api/distancematrix/json?"
    url=base_url+"key="+api_key+"&origins="+originLat+","+originLon+"&destinations="+destLat+","+destLon
    data = requests.get(url)
    jsonData=data.json()
    new = dumps(jsonData)
    newest = yaml.safe_load(new)
    #print newest
    return newest["rows"][0]["elements"][0]["distance"]["text"]

def getNearbyRestaurantsUsingCoord(lat,lon):
    final=""
    txtheaders={'Accept': 'application/json', 'user-key': '8fd3c44cc71fec43d7523c4ef89c31fa'}
    api_key="8fd3c44cc71fec43d7523c4ef89c31fa"
    base_url="https://developers.zomato.com/api/v2.1/search?"
    sort="real_distance"
    txtdata=None
    #url=base_url+"api_key="+api_key+"&lat="+lat+"&lon="+lon+"&sort="+sort+"&order=asc"
    url="https://developers.zomato.com/api/v2.1/geocode?lat=12.8446784&lon=77.6610528"
    data = urllib2.Request(url,txtdata,txtheaders)
    dat=urllib2.urlopen(data)
    dat= json.load(dat)
    dat = dumps(dat)
    finalData = yaml.safe_load(dat)
    final=final+"1)"+finalData["nearby_restaurants"]["1"]["restaurant"]["name"] + " Price(for2):"+ str(finalData["nearby_restaurants"]["1"]["restaurant"]["average_cost_for_two"])+" " +getDist(lat,lon, finalData["nearby_restaurants"]["1"]["restaurant"]["location"]["latitude"], finalData["nearby_restaurants"]["1"]["restaurant"]["location"]["longitude"])+"\n"
    final=final+"2)"+finalData["nearby_restaurants"]["2"]["restaurant"]["name"] + " Price(for2):"+ str(finalData["nearby_restaurants"]["2"]["restaurant"]["average_cost_for_two"])+" " +getDist(lat,lon, finalData["nearby_restaurants"]["2"]["restaurant"]["location"]["latitude"], finalData["nearby_restaurants"]["2"]["restaurant"]["location"]["longitude"])+"\n"
    final=final+"3)"+finalData["nearby_restaurants"]["3"]["restaurant"]["name"] + " Price(for2):"+ str(finalData["nearby_restaurants"]["3"]["restaurant"]["average_cost_for_two"])+" " +getDist(lat,lon, finalData["nearby_restaurants"]["3"]["restaurant"]["location"]["latitude"], finalData["nearby_restaurants"]["3"]["restaurant"]["location"]["longitude"])+"\n"
    final=final+"4)"+finalData["nearby_restaurants"]["4"]["restaurant"]["name"] + " Price(for2):"+ str(finalData["nearby_restaurants"]["4"]["restaurant"]["average_cost_for_two"])+" " +getDist(lat,lon, finalData["nearby_restaurants"]["4"]["restaurant"]["location"]["latitude"], finalData["nearby_restaurants"]["4"]["restaurant"]["location"]["longitude"])+"\n"
    final=final+"5)"+finalData["nearby_restaurants"]["5"]["restaurant"]["name"] + " Price(for2):"+ str(finalData["nearby_restaurants"]["5"]["restaurant"]["average_cost_for_two"])+" " +getDist(lat,lon, finalData["nearby_restaurants"]["5"]["restaurant"]["location"]["latitude"], finalData["nearby_restaurants"]["5"]["restaurant"]["location"]["longitude"])
    return final
    #jsonData=data.json()
    #print jsonData

def getNearbyRestaurantsUsingLoc(loc):
    api_key="AIzaSyDCxrDO4MC2N4H30q7iTfge2hGQLe14kuE"
    base_url="https://maps.googleapis.com/maps/api/geocode/json?"
    url=base_url+"key="+api_key+"&address="+loc
    data = requests.get(url)
    jsonData=data.json()
    new = dumps(jsonData)
    newest = yaml.safe_load(new)
    return getNearbyRestaurantsUsingCoord(str(newest["results"][0]["geometry"]["location"]["lat"]), str(newest["results"][0]["geometry"]["location"]["lng"]))
    # print newest

#print getNearbyRestaurantsUsingLoc("Infosys gate-1, bangalore")
#print getNearbyRestaurantsUsingCoord(lat,lon)
