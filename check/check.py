import os
os.environ.clear()

import psycopg2
print("Connection successfull!")
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="postgres",
    port=5432
)
print("Connection successfull!")
