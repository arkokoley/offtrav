import requests
import yaml
import re
from json import load, dumps

def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext

def getDirections(type, start, end):
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
	final=""
	newest = yaml.safe_load(new)
	init = newest['routes'][0]["legs"][0]["start_address"].split(",")
	dest = newest['routes'][0]["legs"][0]["end_address"].split(",")
	if type=="geo":
		print "CurrentLoc:"+init[-5]+","+init[-4]
	else:
		print "CurrentLoc:"+init[0]
	print "Dest:"+dest[0]
	i=0;
	for eachStep in newest['routes'][0]["legs"][0]["steps"]:
		i=i+1
		if eachStep["travel_mode"]=="TRANSIT":
			final=final+ str(i)+")"+eachStep["transit_details"]["line"]["vehicle"]["type"]+"\n"
			final=final+ eachStep["html_instructions"]+"\n"
			if eachStep["transit_details"]["line"]["vehicle"]["type"]=="BUS":
				final=final+ "From:"+eachStep["transit_details"]["departure_stop"]["name"]+" "+"\n"
				final=final+ "To:"+eachStep["transit_details"]["arrival_stop"]["name"]+"\n"
				if "short_name" in eachStep["transit_details"]["line"]:
					final=final+ "Using:"+eachStep["transit_details"]["line"]["short_name"]+" "+eachStep["transit_details"]["departure_time"]["text"]+"\n"
				else:
					final=final+ "Using:"+eachStep["transit_details"]["line"]["name"]+" "+eachStep["transit_details"]["departure_time"]["text"]+"\n"
			if ((eachStep["transit_details"]["line"]["vehicle"]["type"]=="HEAVY_RAIL")|(eachStep["transit_details"]["line"]["vehicle"]["type"]=="RAIL")):
				final=final+ "From:"+eachStep["transit_details"]["departure_stop"]["name"]+" "+"\n"
				final=final+ "To:"+eachStep["transit_details"]["arrival_stop"]["name"]+"\n"
				final=final+ "Using:"+eachStep["transit_details"]["line"]["name"]+" "+eachStep["transit_details"]["departure_time"]["text"]+"\n"
		if eachStep["travel_mode"]=="WALKING":
			final=final+ str(i)+")"+eachStep["travel_mode"]+"\n"
			temp=eachStep["html_instructions"].split(",")
			final=final+ temp[0]+"\n"
		if "steps" in eachStep:
			final=final+ "for which:"+"\n"
			for every in eachStep["steps"]:
				if "html_instructions" in every:
					final=final+ every["html_instructions"]+"\n"
	return final

print getDirections("geo", "12.9170538,77.67104309999999","Central Silk Boar")
