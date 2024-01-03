import xmlrpc.client

from decimal import Decimal
#from XML.softDeleteExp import deleteData

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

while True:
    print("-----Menu------")
    print("1-Converter ficheiro")
    print("2-Inserir ficheiro na base de dados")
    print("3-Eliminar Ficheiro")
    print("4-Jogos do mundial")
    print("5-Jogos de uma seleção")
    print("6-Cidade e País com mais jogos")
    print("7-Total de golos de uma seleção")
    print("8-Total de golos do Europeu")
    print("9-Média de golos de todos os jogos de seleções")
    print("0-Sair")
    print("\n\n")
    #try:
    option = int(input("Escolha uma opção: "))
    if option == 1:
        print("Converter Para XML")
        print("Nome Do Ficheiro")
        aux = input()
        server.converter(aux)
        pass
    elif option == 2:
        print("Inserir ficheiro na BD")
        print("Nome do ficheiro a ler: ")
        aux = input()
        print("Nome do ficheiro na BD: ")
        aux2 = input()
        server.insertData(aux, aux2)
    elif option == 3:
        print("Delete Data")
        print("Nome do ficheiro")
        aux = input()
        server.deleteData(aux)

        pass

    elif option == 4:
        print("Equipa: ")
        equipa = input()
        a = server.jogos_fora(equipa)
        aux = server.get_connection(a)
        print("Total de jogos Fora da equipa:", aux)

    elif option == 5:
        a = server.total_vitorias()
        aux = server.get_connection(a)
        print("Nº de vitorias por equipas:")
        for row in aux:
            print(row)

    elif option == 6:
        a = server.result_jogos()
        aux = server.get_connection(a)
        print("Resultados de todos os jogos:")
        for row in aux:
            print(row)

    elif option == 7:
        print("Indique dois clubes")
        print("Clube Visitado:")
        home = input()
        print("Clube Visitante:")
        away = input()
        a = server.datas_jogos(home, away)
        aux = server.get_connection(a)
        print("Datas dos jogos")
        for row in aux:
            print(row)

    elif option == 8:
        a = server.media_golos()
        aux = str(server.get_connection(a))
        print("Media de golos de todos os jogos:")
        print(aux)

    elif option == 9:
        a = server.count_jogos()
        aux = server.get_connection(a)
        print("Nº de vitorias em casa, empates e vitorias fora")
        print(aux)

    elif option == 0:
        print("A sair ...")
        break
    #except Exception as e:
        print("Opcao Invalida!!!")