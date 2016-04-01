import requests
import yaml
import re
from json import load, dumps

def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext

def getDirections(start, end):
	api_key="AIzaSyDCxrDO4MC2N4H30q7iTfge2hGQLe14kuE"
	base_url="https://maps.googleapis.com/maps/api/directions/json?"
	url=base_url+"key="+api_key
	origin=start
	destination=end
	mode="transit"
	url=url+"&origin="+origin+"&destination="+destination+"&mode="+mode+"&alternatives=true"+"&departure_time=now"
	data = requests.get(url)
	jsonData=data.json()
	new = dumps(jsonData)
	new=cleanhtml(new)
	newest = yaml.safe_load(new)
	init = newest['routes'][0]["legs"][0]["start_address"].split(",")
	final = newest['routes'][0]["legs"][0]["end_address"].split(",")
	print "CurrentLoc:"+init[0]
	print "Dest:"+final[0]
	i=0;
	for eachStep in newest['routes'][0]["legs"][0]["steps"]:
		i=i+1
		if eachStep["travel_mode"]=="TRANSIT":
			print str(i)+")"+eachStep["transit_details"]["line"]["vehicle"]["type"]
			print eachStep["html_instructions"]
			if eachStep["transit_details"]["line"]["vehicle"]["type"]=="BUS":
				print "From:"+eachStep["transit_details"]["departure_stop"]["name"]+" "
				print "To:"+eachStep["transit_details"]["arrival_stop"]["name"]
				if "short_name" in eachStep["transit_details"]["line"]:
					print "Using:"+eachStep["transit_details"]["line"]["short_name"]+" "+eachStep["transit_details"]["departure_time"]["text"]
				else:
					print "Using:"+eachStep["transit_details"]["line"]["name"]+" "+eachStep["transit_details"]["departure_time"]["text"]
			if ((eachStep["transit_details"]["line"]["vehicle"]["type"]=="HEAVY_RAIL")|(eachStep["transit_details"]["line"]["vehicle"]["type"]=="RAIL")):
				print "From:"+eachStep["transit_details"]["departure_stop"]["name"]+" "
				print "To:"+eachStep["transit_details"]["arrival_stop"]["name"]
				print "Using:"+eachStep["transit_details"]["line"]["name"]+" "+eachStep["transit_details"]["departure_time"]["text"]
		if eachStep["travel_mode"]=="WALKING":
			print str(i)+")"+eachStep["travel_mode"]
			temp=eachStep["html_instructions"].split(",")
			print temp[0]
		if "steps" in eachStep:
			print "for which:"
			for every in eachStep["steps"]:
				if "html_instructions" in every:
					print every["html_instructions"]

getDirections("Whitefield, Bangalore","Central Silk Boar")
