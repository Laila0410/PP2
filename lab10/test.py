import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres",
                        password="postgres", port=5432, client_encoding="utf-8")   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists snake(
            name VARCHAR(255),
            level INTEGER,
            score INTEGER
);
           """)