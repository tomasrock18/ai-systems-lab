"""
Искал решение без помощи ИИ, только справочные данные из поиска.

"""
import concurrent.futures

import psycopg2


def func():
    conn = psycopg2.connect(
        "dbname=kovs-db user=kovs host=localhost port=5432 password=112233"
    )
    cur = conn.cursor()

    for _ in range(1000):
        cur.execute("SELECT * FROM counter")
        value = cur.fetchall()[0][1]

        cur.execute(f"UPDATE counter SET value = {value + 1} WHERE id = 1")
        conn.commit()


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for _ in range(2):
            future = executor.submit(func)
