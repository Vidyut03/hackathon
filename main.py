import sqlite3 as sql
from sqlite3 import Error
import os
import json

def create_connection(db):
  conn = None
  try:
    conn = sql.connect(db)
    print('DB Connected')
  except Error as e:
    print('Error:',e)
  
  return conn

def process_file(conn, file):
  file = 'json-files/AC2-07337-anon.json'
  data = json.load(open(file))
  elements = ['Index', 'WorkOrder', 'PartNumber', 'PartDescription', 'ToolLocation', 'Comment1', 'Comment2', 'Comment3', 'PartTCs', 'PartProbes', 'OtherSensors', 'EntryName']
  x = data['PartInformation']
  for part_info in x:
    l=[]
    for element in elements:
      l.append(part_info[element])
    l.append(file)
    add_part_info(conn, l)

  elements = ['FileName', 'FilePath', 'LoadNumber', 'Equipment', 'RunRecipe', 'RunStart', 'RunEnd', 'RunDuration', 'OperatorName', 'ExportControl', 'EntryName']
  x = data['RunDetails']
  l=[]
  for element in elements:
    l.append(x[element])
  l.append(file)
  add_run_detail(conn, l)

def add_run_detail(conn, l):
  pass

def add_part_info(conn, l):
  pass

def main():
  # db = 'db/tmp.db'
  # conn = create_connection(db)
  # if conn:
  #   pass
  # else:
  #   print('DB connection failed')
  for file in os.listdir('json-files/'):
    process_file(conn, file)

if __name__ == '__main__':
  main()