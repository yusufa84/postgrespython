import psycopg2
from config_reader import config

def dbconnect():
    try:
        conn = None
        params = config()
        print('Connecting to the PostgreSQL database')
        conn = psycopg2.connect(**params)
        print('Database connected successfully')
        cur = conn.cursor()
        print('PostgreSQL version: ')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')


if __name__ == '__main__':
    dbconnect()