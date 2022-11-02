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

def create_table(conn, statement):
  try:
    c = conn.cursor()
    c = c.execute(statement)
  except Error as e:
    print('Error:', e)

def main():
  db = '/home/mohish/studio2/hackathon/hackathon/db/tmp.db'
  create_run_details_table = open('run_details.sql', 'r').read()
  # create_part_info_table = open('part_info.sql', 'r').read()
  conn = create_connection(db)
  if conn:
    create_table(conn, create_run_details_table)
    create_table(conn, create_part_info_table)
  else:
    print('DB connection failed')

if __name__ == '__main__':
  main()