import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="postgres",
    port=5432
)
print("Connection successful!")
