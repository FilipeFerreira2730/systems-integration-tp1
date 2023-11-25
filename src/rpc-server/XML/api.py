from urllib import parse, request
import json

def get_data(city):
    params = parse.urlencode({
         'city' : city,
         'country' : 'UK',
         'format' : 'jsonv2'
    })
    with request.urlopen(f'https://nominatim.openstreetmap.org/search?{params}') as req:
        data = json.loads(req.read())
        return data