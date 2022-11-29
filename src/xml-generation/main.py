import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from entities.country import Country
from entities.team import Team
from entities.player import Player


class XMLFileReader:

    def __init__(self, path, delimiter=','):
        self._path = path
        self._delimiter = delimiter

    def loop(self):
        with open(self._path, 'r') as file:
            for row in csv.DictReader(file, delimiter=self._delimiter):
                yield row
        file.close()

    def read_entities(self, name, attr, builder, after_create = None):
        #print(f"reading {name} objects...")

        entities = {}
        for row in self.loop():
            e = row[attr]
            if e not in entities:
                entities[e] = builder(row)
                after_create is not None and after_create(entities[e], row)

        #print(f"There are {len(entities)} unique {name} objects")
        return entities


class DatasetCSVtoXMLConverter:

    def __init__(self, path):
        self._reader = XMLFileReader(path)

    def to_xml(self):
        # read countries
        countries = self._reader.read_entities(
            name="country",
            attr="nationality",
            builder=lambda row: Country(row["nationality"]),
            #after_create=lambda country, row: print(f"> {country}")
        )

        # read teams
        teams = self._reader.read_entities(
            name="team",
            attr="Current Club",
            builder=lambda row: Team(row["Current Club"]),
            #after_create=lambda team, row: print(f"> {team}")
        )

        # read players

        def after_creating_player(player, row):
            # add the player to the appropriate team
            teams[row["Current Club"]].add_player(player)
            #print(f"> {player}")

        players = self._reader.read_entities(
            name="player",
            attr="full_name",
            builder=lambda row: Player(
                name=row["full_name"],
                age=row["age"],
                country=countries[row["nationality"]]
            ),
            after_create=after_creating_player
        )

        # generate the final xml
        root_el = ET.Element("Football")

        teams_el = ET.Element("Teams")
        for team in teams.values():
            teams_el.append(team.to_xml())

        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        root_el.append(teams_el)
        root_el.append(countries_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()


if __name__ == "__main__":
    converter = DatasetCSVtoXMLConverter("/data/sample_dataset.csv")
    print(converter.to_xml_str())