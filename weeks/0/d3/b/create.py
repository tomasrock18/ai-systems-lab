"""
Искал решение без помощи ИИ, только справочные данные из поиска.

"""
import psycopg2

conn = psycopg2.connect(
    "dbname=kovs-db user=kovs host=localhost port=5432 password=112233"
)
cur = conn.cursor()

cur.execute(
    "CREATE TABLE counter (id INTEGER PRIMARY KEY, value INTEGER NOT NULL);"
    "INSERT INTO counter VALUES (1, 0)"
)
conn.commit()
