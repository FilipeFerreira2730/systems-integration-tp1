from urllib import parse, request
import json

def get_data(city, country):
    params = parse.urlencode({
         'city': city,
         'country': country,
         'format': 'jsonv2'
    })
    with request.urlopen(f'https://nominatim.openstreetmap.org/search?{params}') as req:
        data = json.loads(req.read())
        return data
