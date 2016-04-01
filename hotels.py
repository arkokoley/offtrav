from amadeus import Hotels
from json import dumps
import yaml
import re
import requests
def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext
hotels = Hotels('tkGbmBwS846vek2wKrtt22E3Pp72lUAC')
resp = hotels.search_circle(
	check_in='2016-04-02',
	check_out='2016-04-04',
	latitude = 12.9279,
	longitude = 77.6271,
	currency='INR',
	radius=2
	)
new = dumps(resp)
newest = yaml.safe_load(new)
l = [] 
#print len(newest['results'])
value = len(newest['results'])
#print value
for i in range(0,value):
	#+eachStep["travel_mode"]

	print newest['results'][i]['total_price']
	l.append(newest['results'][i]['total_price'])
	print newest['results'][i]['property_name']
	#print eachStep['total_price']
	#print eachStep['total_price']
	#print eachStep['property_name']

j=1;
if(j==1):
	print newest['results'][j]['property_name']
	print newest['results'][j]['address']
	print newest['results'][j]['contacts']




api_key="tkGbmBwS846vek2wKrtt22E3Pp72lUAC"
base_url="https://api.sandbox.amadeus.com/v1.2/hotels/"
url=base_url
origin="2016-04-03"
destination="2016-04-04"
pcode="RTNCEPUL"
url=url+pcode+"?check_in="+origin+"&check_out="+destination+"&apikey="+api_key
data = requests.get(url)
jsonData=data.json()
new = dumps(jsonData)
#new=cleanhtml(new)
newest = yaml.safe_load(new)
print newest['property_name']

	