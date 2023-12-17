import psycopg2

connection = None
cursor = None

def get_connection(query):
    connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="is-db",
                                  port="5432",
                                  database="is")

    with connection.cursor() as cursor:
        print(cursor)
        cursor.execute(query)
        aux = cursor.fetchall()

        return aux
