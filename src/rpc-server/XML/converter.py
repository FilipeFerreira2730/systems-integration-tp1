import csv
from wsgiref.validate import validator
from xml.etree.ElementTree import ElementTree, Element, SubElement
from XML.api import get_data


def converter(filename):
    with open('/assets/eplmatches.csv') as file:
        csv_f = csv.DictReader(file)
        data = []

        root = Element('premierLeague')
        years = {}

        ano = None
        jornada = None

        for num, row in enumerate(csv_f):
            if num == 20000:
                break
            print(row)

            # verificar se o ano existe
            season_year = row['Season_End_Year']

            if season_year not in years:
                years[season_year] = len(years) + 1

            if ano is None or ano != row['Season_End_Year']:
                ano = row['Season_End_Year']
                season = SubElement(root, 'Season_End_Year', {
                    'id': str(years[season_year])
                })

            if jornada is None or jornada != row['Wk']:
                jornada = row['Wk']
                week = SubElement(season, 'Wk', {
                    'num': row['Wk']
                })

            game = SubElement(week, 'game', {
                'id': str(num + 1)
            })

            date = SubElement(game, 'Date')
            date.text = row['Date']

            home = SubElement(game, 'Home')
            home.text = row['Home']

            homegoals = SubElement(game, 'HomeGoals')
            homegoals.text = row['HomeGoals']

            awayGoals = SubElement(game, 'AwayGoals')
            awayGoals.text = row['AwayGoals']

            away = SubElement(game, 'Away')
            away.text = row['Away']

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
        et.write(f'{filename}.xml')
        validator(filename)