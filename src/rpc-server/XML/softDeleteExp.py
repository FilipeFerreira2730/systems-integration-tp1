import psycopg2


def deleteData(file_name):
    connection = None
    cursor = None

    try:
        with psycopg2.connect(user="is",
                                      password="is",
                                      host="localhost",
                                      port="10001",
                                      database="is") as connection:

            with connection.cursor() as cursor:
                a = cursor.execute("UPDATE imported_documents SET isdeleted = true WHERE file_name = %s", (file_name, ))


    except (Exception, psycopg2.Error) as error:
        print('aaaaaa', error)
        print("Failed to fetch data", error)

    finally:
            connection.close()
