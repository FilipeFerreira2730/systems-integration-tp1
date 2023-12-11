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
    print("6-Cidade e País com mais jogos") """rever esta querie"""
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
        aux=server.string_reverse("O gestor é lindo")
        print(aux)

        pass


    elif option == 0:
        print("A sair ...")
        break
    #except Exception as e:
        print("Opcao Invalida!!!")