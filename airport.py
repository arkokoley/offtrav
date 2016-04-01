from amadeus import Hotels

hotels = Hotels('<Your API Key>')
resp = hotels.search_airport(
    check_in='2015-11-25',
    check_out='2015-11-30',
    location='BKK',
    currency='USD',
    max_rate=100)
print(resp)