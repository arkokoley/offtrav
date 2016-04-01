from amadeus import Hotels
from json import dumps
import yaml
import re
import requests
def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext

def getHotels(start, end):
	hotels = Hotels('tkGbmBwS846vek2wKrtt22E3Pp72lUAC')
	resp = hotels.search_circle(
		check_in=start,
		check_out=end,
		latitude = 12.9279,
		longitude = 77.6271,
		currency='INR',
		radius=2
		)
	new = dumps(resp)
	newest = yaml.safe_load(new)
	l = [] 
	final=""
	#print len(newest['results'])
	value = len(newest['results'])
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

print getHotels("2016-04-02","2016-04-04")


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

print getHotel("2016-04-02","2016-04-04","YXBLRACE")