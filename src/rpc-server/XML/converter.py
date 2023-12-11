import csv
from pkgutil import get_data
#from wsgiref.validate import validator
from xml.etree.ElementTree import ElementTree, Element, SubElement
from datetime import datetime
from api import get_data

def converter(filename):
    with open('/data/test.csv') as file:
        csv_f = csv.DictReader(file)
        data = []

        root = Element('Jogoselecao')
        years = {}
        games = {}

        ano = None
        count = 0
        for num, row in enumerate(csv_f):
            count = count + 1
            if num == 20000:
                break
            print(row)

            # Extract the year from the date
            game_date = row['date']
            game_year = datetime.strptime(game_date, '%Y-%m-%d').year

            if game_year not in years:
                years[game_year] = len(years) + 1

            if ano is None or ano != game_year:
                ano = game_year
                season = SubElement(root, 'game_End_Year', {
                    'id': str(years[game_year])
                })

            game = SubElement(season, 'game', {
                'id': str(num + 1)
            })

            date = SubElement(game, 'date')
            date.text = row['date']

            home_team = SubElement(game, 'Home_team')
            home_team.text = row['home_team']

            away_team = SubElement(game, 'Away_team')
            away_team.text = row['away_team']

            home_score = SubElement(game, 'Home_score')
            home_score.text = row['home_score']

            away_score = SubElement(game, 'Away_score')
            away_score.text = row['away_score']

            tournament_element = SubElement(game, 'Tournament')
            tournament_element.text = row['tournament']

            if num < count:
                city = row['city']
                country = row['country']

                # Use city and country to get data (modify get_data function accordingly)
                data = get_data(city, country)

                if len(data) > 0:
                    coordinates = SubElement(game, "Coordinates", {
                        'lat': data[0]['lat'],
                        'lon': data[0]['lon']
                    })
                    city_element = SubElement(coordinates, 'City')
                    city_element.text = city
                    country_element = SubElement(coordinates, 'Country')
                    country_element.text = country

        y = SubElement(root, 'Years')

        for data, season in years.items():
            yy = SubElement(y, 'Year', {
                'id': str(season)
            })
            yy.text = str(data)

        et = ElementTree(root)
        et.write(f'{filename}.xml')