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
    print("4-Jogos de uma equipa em casa")
    print("5-Todos os jogos num ano")
    print("6-Resultados dos jogos")
    print("7-Total de golos da competição")
    print("8-Media de golos de uma equipa")
    print("9-Numero total de vitorias")
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
        a = server.jogos_casa(equipa)
        aux = server.get_connection(a)
        print("Jogos da equipa em casa:", aux)

    elif option == 5:
        print("Ano: ")
        ano = input()
        a = server.jogos_ano(ano)
        aux = server.get_connection(a)
        print("Jogos no ano:", aux)

    elif option == 6:
        a = server.resultado_jogos()
        aux = server.get_connection(a)
        print("Resultados dos jogos:")
        for row in aux:
            print(row)

    elif option == 7:
        a = server.total_golos()
        aux = server.get_connection(a)
        print("Total de golos:")
        print(aux)

    elif option == 8:
        print("Equipa: ")
        equipa = input()
        a = server.media_golos_equipa(equipa)
        aux = server.get_connection(a)
        print("Media de golos de todos os jogos:", aux)
        print(aux)

    elif option == 9:
        a = server.numero_vitorias()
        aux = server.get_connection(a)
        print("Numero total de vitorias")
        print(aux)

    elif option == 0:
        print("A sair ...")
        break
    #except Exception as e:
        print("Opcao Invalida!!!")