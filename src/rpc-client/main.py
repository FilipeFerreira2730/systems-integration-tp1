import xmlrpc.client

from decimal import Decimal
#from XML.softDeleteExp import deleteData

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

while True:
    print("-----Menu------")
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