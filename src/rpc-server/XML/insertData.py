import psycopg2


def insertData(read,filename):
    connection = None
    cursor = None

    try:
        with psycopg2.connect(user="is",
                              password="is",
                              host="localhost",
                              port="5432",
                              database="is") as connection:

            with connection.cursor() as cursor:
                with open(f'/usr/src/app/rpc-server/XML/{read}.xml') as f:
                    file_data = f.read()

                    print(filename)
                    cursor.execute("INSERT INTO imported_documents(file_name, xml) VALUES (%s, %s)",
                                   (filename, file_data, ))



    except (Exception, psycopg2.Error) as error:
        print('Erro:', error)
        print("Failed to fetch data", error)

    finally:
        connection.close()
