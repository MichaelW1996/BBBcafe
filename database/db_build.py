# open connection to db in docker container localhost:5433
import psycopg2


def connect():
    conn = psycopg2.connect(
        dbname='bbb_db',
        user='bbb_group',
        password='password',
        host='localhost',
        port='5433'
    )
    return conn

# use schema.sql to create tables

def create_tables():
    conn = connect()
    cur = conn.cursor()
    with open('schema.sql', 'r') as f:
        cur.execute(f.read())
    conn.commit()
    conn.close()

create_tables()