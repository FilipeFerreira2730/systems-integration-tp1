def jogos_casa(equipa):

    a = (f"select unnest(xpath('count(/premierLeague/Season_End_Year/Wk/game[Home=\"{equipa}\"])', xml)) "
            f"from imported_documents where file_name = 'output.xml';")
    return a

def jogos_ano(ano):
    a = (f"select unnest(xpath('//premierLeague/Season_End_Year[@id=\"{ano}\"]/Wk/game', xml)), "
         f"count(*) as number_of_games "
         f"from imported_documents where file_name = 'output.xml'")
    return a

def resultado_jogos():
    a = (f"select home,away,home_goals || '-' || away_goals as score from ("
         f"select unnest(xpath('/premierLeague/Season_End_Year/Wk/game/Home/text()', xml))::text as home,"
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/Away/text()', xml))::text as away,"
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/HomeGoals/text()', xml))::text as home_goals,"
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/AwayGoals/text()', xml))::text as away_goals "
         f"from imported_documents where file_name = 'output.xml') as t;")
    return a

def total_golos():
    a = (f"select sum(home_goals + away_goals) as total_golos from ("
         f"select unnest(xpath('//premierLeague/Season_End_Year/Wk/game/HomeGoals/text()', xml))::int as home_goals, "
         f"unnest(xpath('//premierLeague/Season_End_Year/Wk/game/AwayGoals/text()', xml))::int as away_goals "
         f"from imported_documents where file_name = 'output.xml') as jogos")
    return a

def media_golos_equipa(equipa):
    query = (f"select avg(golos::float) as media_golos from ("
             f"select home_goals::int as golos from ("
             f"select unnest(xpath('//premierLeague/Season_End_Year/Wk/game[Home=\"{equipa}\"]/HomeGoals/text()', xml)) as home_goals "
             f"from imported_documents where file_name = 'output.xml') "
             f"union all "
             f"select away_goals::int as golos from ("
             f"select unnest(xpath('//premierLeague/Season_End_Year/Wk/game[Away=\"{equipa}\"]/AwayGoals/text()', xml)) as away_goals "
             f"from imported_documents where file_name = 'output.xml') "
             f") as jogos")
    return query


def media_golos_equipa(equipa):
    a = (
        f"select avg(golos::float) as media_golos from ("
        f"select unnest(xpath('//premierLeague/Season_End_Year/Wk/game[Home=\"{equipa}\"]/HomeGoals/text()', xml))::int as golos "
        f"union all  "
        f"select unnest(xpath('//premierLeague/Season_End_Year/Wk/game[Away=\"{equipa}\"]/AwayGoals/text()', xml))::int "
        f") as jogos, imported_documents where file_name = 'output.xml'"
    )
    return a


def numero_vitorias():
    a = (f"select (xpath('count(//premierLeague/Season_End_Year/Wk/game/FTR[text()=\"H\"])', xml)::text::int)[1] as numVCasa, "
         f"(xpath('count(//premierLeague/Season_End_Year/Wk/game/FTR[text()=\"A\"])', xml)::text::int)[1] as numVFora, "
         f"(xpath('count(//premierLeague/Season_End_Year/Wk/game/FTR[text()=\"H\"])', xml)::text::int)[1] + "
         f"(xpath('count(//premierLeague/Season_End_Year/Wk/game/FTR[text()=\"A\"])', xml)::text::int)[1] as totalVitorias "
         f"from imported_documents where file_name = 'output.xml';")
    return a

