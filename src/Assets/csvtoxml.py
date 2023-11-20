import csv
from pkgutil import get_data
from wsgiref.validate import validator
from xml.etree.ElementTree import ElementTree, Element, SubElement

def converter(filename):
    with open('/assets/IS.csv') as file:
        csv_f = csv.DictReader(file)
        data = []

        root = Element('Jogoselecao')
        years = {}
        games = {}

        ano = None

        for num, row in enumerate(csv_f):
            if num == 20000:
                break
            print(row)

            # verificar se o ano existe
            game_year = row['game_End_Year']

            if game_year not in years:
                years[game_year] = len(years) + 1

            if ano is None or ano != row['game_End_Year']:
                ano = row['Season_End_Year']
                season = SubElement(root, 'game_End_Year', {
                    'id': str(years[game_year])
                })

            game = SubElement('game', {
                'id': str(num + 1)
            })

            date = SubElement(game, 'Date')
            date.text = row['Date']

            home_team = SubElement(game, 'Home_team')
            home_team.text = row['Home_team']

            away_team = SubElement(game, 'Away_team')
            away_team.text = row['Away_team']

            home_score = SubElement(game, 'Home_score')
            home_score.text = row['Home_score']

            away_score = SubElement(game, 'Away_score')
            away_score.text = row['Away_score']

            ftr = SubElement(game, 'FTR')
            ftr.text = row['FTR']

            if num < 1:
                city = row['Home'].split()
                data = get_data(city[0])
                if len(data) > 0:
                    coordinates = SubElement(game, "Coordinates", {
                        'lat': data[0]['lat'],
                        'lon': data[0]['lon']
                    })

        y = SubElement(root, 'Years')

        for data, season in years.items():
            yy = SubElement(y, 'Year', {
                'id': str(season)
            })
            yy.text = str(data)

        et = ElementTree(root)
        et.write(f'./rpc-server/XML/{filename}.xml')
        validator(filename)