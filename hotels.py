from amadeus import Hotels
from json import dumps
import yaml
import re
import requests
def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext
def getlatlong(location):
    api_key="AIzaSyDCxrDO4MC2N4H30q7iTfge2hGQLe14kuE"
    base_url="https://maps.googleapis.com/maps/api/geocode/json?"
    url=base_url+"key="+api_key+"&address="+location
    data = requests.get(url)
    jsonData=data.json()
    new = dumps(jsonData)
    newest = yaml.safe_load(new)
    coord = []
    coord.append(newest["results"][0]["geometry"]["location"]["lat"])
    coord.append(newest["results"][0]["geometry"]["location"]["lng"])
    return coord
    # print newest  

print getlatlong("Central Silk Board")
temp=getlatlong("Central Silk Board")
print temp[0]
print temp[1]

def getHotels(start, end,lat,log):
	hotels = Hotels('tkGbmBwS846vek2wKrtt22E3Pp72lUAC')
	resp = hotels.search_circle(
		check_in=start,
		check_out=end,
		latitude = lat,
		longitude = log,
		currency='INR',
		radius=2
		)
	new = dumps(resp)
	newest = yaml.safe_load(new)
	l = []
	final=""
	#print len(newest['results'])
	value = len(newest['results'])
	if(value>=5):
		value=5
	elif(value<5):
		value=len(newest['results'])

	#print value
	for i in range(0,value):
		#+eachStep["travel_mode"]
		final=final+ "Total Price:"+newest['results'][i]['total_price']['amount']+" "+"\n"
		final=final+ "Currency Mode:"+newest['results'][i]['total_price']['currency']+" "+"\n"
		final=final+ "Currency Mode:"+newest['results'][i]['property_name']+" "+"\n"
		#print eachStep['total_price']
		#print eachStep['total_price']
		#print eachStep['property_name']

	#j=1;
	#if(j==1):
	#	print newest['results'][j]['property_name']
	#	print newest['results'][j]['address']
	#	print newest['results'][j]['contacts']

	return final

print getHotels("2016-04-02","2016-04-04",temp[0],temp[1])

def getHotelCode(start,end,lat,log,number):
	hotels = Hotels('tkGbmBwS846vek2wKrtt22E3Pp72lUAC')
	resp = hotels.search_circle(
		check_in=start,
		check_out=end,
		latitude = lat,
		longitude = log,
		currency='INR',
		radius=2
		)
	new = dumps(resp)
	newest = yaml.safe_load(new)
	return newest['results'][number]['property_code']

print getHotelCode("2016-04-02","2016-04-04",temp[0],temp[1],0)
def getHotel(start, end, code):
	api_key="tkGbmBwS846vek2wKrtt22E3Pp72lUAC"
	base_url="https://api.sandbox.amadeus.com/v1.2/hotels/"
	url=base_url
	origin=start
	destination=end
	pcode=code
	final=""
	url=url+pcode+"?check_in="+origin+"&check_out="+destination+"&apikey="+api_key
	data = requests.get(url)
	jsonData=data.json()
	new = dumps(jsonData)
	#new=cleanhtml(new)
	newest = yaml.safe_load(new)
	final=final+ "Particular Hotel Currency:"+newest['total_price']['currency']+" "+"\n"
	final=final+ "Particular Hotel Total Price:"+newest['total_price']['amount']+" "+"\n"
	final=final+ "Particular Hotel Name:"+newest['property_name']+" "+"\n"
	final=final+ "Location - Latitude :"+str(newest['location']['latitude'])+" "+"Longitude :"+str(newest['location']['longitude'])+" "+"\n"
	return final

print getHotel("2016-04-02","2016-04-04", str(getHotelCode("2016-04-02","2016-04-04",temp[0],temp[1],0)))


