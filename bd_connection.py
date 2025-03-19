import psycopg2


def get_connection():
    return psycopg2.connect(
        database="hospital-persistencia",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )