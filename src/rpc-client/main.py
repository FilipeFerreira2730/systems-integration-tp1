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
        server.insertData(aux,aux2)
    elif option == 3:
        print("Delete Data")
        print("Nome do ficheiro")
        aux = input()
        server.deleteData(aux)
    elif option == 4:
        a = server.jogos_mundial()
        aux = server.get_connection(a)
        print("Jogos do mundial:", aux)
    elif option == 5:
        print("Selecao: ")
        selecao = input()
        a = server.jogos_fora(selecao)
        aux = server.get_connection(a)
        print("Jogos da selecao:", aux)
    elif option == 6:
        print("Cidade e País com mais jogos:")
        a = server.cidade_pais_mais_jogos()
        aux = server.get_connection(a)
        print("Cidade e País com mais jogos:", aux)

    elif option == 7:
        print("Total de golos de uma seleção:")
        print("Selecao: ")
        selecao = input()
        a = server.total_golos_selecao(selecao)
        aux = server.get_connection(a)
        print(f"Total de golos de {selecao}:", aux)

    elif option == 8:
        print("Total de golos do Europeu:")
        a = server.total_golos_uefa_euro()
        aux = server.get_connection(a)
        print("Total de golos do Europeu:", aux)

    elif option == 9:
        print("Média de golos de todos os jogos de seleções:")
        a = server.media_golos_todos_jogos()
        aux = server.get_connection(a)
        print("Média de golos de todos os jogos de seleções:", aux)

    elif option == 0:
        print("A sair ...")
        break
    #except Exception as e:
        print("Opcao Invalida!!!")