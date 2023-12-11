def jogos_mundial():
    a = (
        "SELECT unnest(xpath('//game', xml)) "
        "FROM imported_documents WHERE tournament = 'FIFA World Cup';"
    )
    return a

def jogos_selecao(selecao):
    a = (
        f"SELECT unnest(xpath('//game[Home_team=\"{selecao}\" or Away_team=\"{selecao}\"]', xml)) "
        f"FROM imported_documents WHERE home_team = '{selecao}' OR away_team = '{selecao}';"
    )
    return a

def cidade_pais_mais_jogos():
    a = (
        f"SELECT unnest(xpath('//city', xml)) as city, "
        f"unnest(xpath('//country', xml)) as country, "
        f"COUNT(*) as num_games "
        f"FROM imported_documents "
        f"GROUP BY city, country "
        f"ORDER BY num_games DESC "
        f"LIMIT 1;"
    )
    return a

def total_golos_selecao(selecao):
    a = (
        f"SELECT '{selecao}' as team, "
        f"SUM(home_score + away_score) as total_goals "
        f"FROM imported_documents "
        f"WHERE home_team = '{selecao}' OR away_team = '{selecao}';"
    )
    return a

def total_golos_uefa_euro():
    a = (
        "SELECT SUM(home_score + away_score) as total_goals "
        "FROM imported_documents "
        "WHERE tournament = 'UEFA Euro';"
    )
    return a


def media_golos_todos_jogos():
    a = (
        "SELECT AVG(home_score + away_score) as average_goals "
        "FROM imported_documents;"
    )
    return a
