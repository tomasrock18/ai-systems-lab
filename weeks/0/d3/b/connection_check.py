"""
Искал решение без помощи ИИ, только справочные данные из поиска.

"""
import time

import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect("dbname=kovs-db user=kovs host=localhost port=5432 password=112233")
    cur = conn.cursor()

    while True:
        cur.execute("SELECT * from pg_stat_activity")
        print(f"\r{len(cur.fetchall())}")
        time.sleep(0.2)
