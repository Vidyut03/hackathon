import sqlite3 as sql
from sqlite3 import Error

def create_connection(db):
  conn = None
  try:
    conn = sql.connect(db)
    print('DB Connected')
  except Error as e:
    print('Error:',e)
  
  return conn

def main():
  db = 'db/tmp.db'
  f = open('Hackathon2.sql', 'r')
  conn = create_connection(db)
  if conn:
    create_table(conn, create_run_details_table)
    # create_table(conn, create_part_info_table)
  else:
    print('DB connection failed')

if __name__ == '__main__':
  main()