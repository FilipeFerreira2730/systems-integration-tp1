

def jogos_fora(equipa):

    a = (f"select unnest(xpath('count(/premierLeague/Season_End_Year/Wk/game[Away=\"{equipa}\"])', xml)) "
            f"from imported_documents where file_name = 'output.xml';")
    return a


def total_vitorias():
    a = f"select unnest(array_cat( xpath('/premierLeague/Season_End_Year/Wk/game[FTR=\"H\"]/Home/text()', xml)::text[]," \
        f" xpath('/premierLeague/Season_End_Year/Wk/game[FTR=\"A\"]/Away/text()', xml)::text[]))    as winners, " \
        f"count(*) as n_wins from imported_documents where file_name = 'output.xml' group by winners order by n_wins desc;"
    return a

def result_jogos():
    a = (f"select home,away,home_goals || '-' || away_goals as score from ("
         f"select unnest(xpath('/premierLeague/Season_End_Year/Wk/game/Home/text()', xml))::text as home,"
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/Away/text()', xml))::text as away,"
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/HomeGoals/text()', xml))::text as home_goals,"
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/AwayGoals/text()', xml))::text as away_goals "
         f"from imported_documents where file_name = 'output.xml') as t;")
    return a

def media_golos():
    a = (f"select avg(score)::float as AverageGoals from (select club, clubAway, home, away, sum(home + away) as score "
         f"from (select unnest(xpath('/premierLeague/Season_End_Year/Wk/game/HomeGoals/text()', xml))::text::int as home, "
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/AwayGoals/text()', xml))::text::int as away, "
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/Home/text()', xml))::text           as club, "
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game/Away/text()', xml))::text           as clubAway "
         f"from imported_documents where file_name = 'output.xml' group by home, away, club, clubAway) as l "
         f"group by l.home, l.away, l.club, l.clubAway) as t;")
    return a

def datas_jogos(home, away):
    a = (f"select dateHome from(select "
         f"unnest(xpath('/premierLeague/Season_End_Year/Wk/game[Home=\"{home}\"][Away=\"{away}\"]/Date/text()', xml))::text "
         f"as dateHome from imported_documents where file_name = 'output.xml' group by dateHome) as r;")
    return a

def count_jogos():
    a = (f"select unnest(xpath('count(/premierLeague/Season_End_Year/Wk/game/FTR[text()= \"H\"])',xml))::text::int as nVitoriasEmcasa,"
    "unnest(xpath('count(/premierLeague/Season_End_Year/Wk/game/FTR[text()= \"D\"])',xml))::text::int as nEmpates,"
         "unnest(xpath('count(/premierLeague/Season_End_Year/Wk/game/FTR[text()= \"A\"])',xml))::text::int as nVitoriasFora "
         "from imported_documents where file_name = 'output.xml' ;"
         )
    return a