import psycopg2


def get_connection(query):
    connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="localhost",
                                  port="5432",
                                  database="is")

    cursor = connection.cursor()

    cursor.execute(query)
    aux = cursor.fetchall()

    return aux