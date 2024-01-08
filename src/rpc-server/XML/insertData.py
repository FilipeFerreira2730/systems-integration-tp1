import psycopg2

def insertData1(read,filename):
    connection = None
    cursor = None



    try:
        with psycopg2.connect(user="is",
                              password="is",
                              host="is-db",
                              port="10001",
                              database="is") as connection:

            with open("./XML/r.txt", 'w') as file:
                # Escrevendo uma linha de texto no arquivo
                file.write("Esta é uma linha de exemplo.\n")

            with connection.cursor() as cursor:
                """with open(f'/usr/src/app/rpc-server/XML/{read}.xml') as f:
                    file_data = f.read()

                    print(filename)
                    cursor.execute("INSERT INTO imported_documents(file_name, xml) VALUES (%s, %s)",
                                   (filename, file_data, ))"""



                cursor.execute("insert into imported_documents(file_name, xml) Values ('porto', 'marega')")
                connection.commit()

    except (Exception, psycopg2.Error) as error:
        print('Erro:', error)
        print("Failed to fetch data", error)

    finally:
        print("mana")
        """connection.close()"""
