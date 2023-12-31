import psycopg2

connection = None
cursor = None

try:
    connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="is-db",
                                  port="10001",
                                  database="is")

    with connection.cursor() as cursor:
        with open('../rpc-server/XML/ols.xml') as f:
            file_data = f.read()
            filename = "marega"
            a = cursor.execute("INSERT INTO imported_documents(file_name, xml) VALUES (%s, %s)", (filename, file_data))

except (Exception, psycopg2.Error) as error:
    print("Failed to fetch data", error)

finally:
    if connection:
        cursor.close()
        connection.close()
