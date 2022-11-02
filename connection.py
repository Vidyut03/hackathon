import sqlite3 as sql
from sql import Error

def create_connection(df):
  conn = None
  try:
    conn = sql.connect(db)
    print('DB Connected')
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()

if __name__ == '__main__':
  db = '/home/mohish/studio2/hackathon/hackathon/db/tmp.db'
  create_connection(db)