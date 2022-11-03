import sqlite3 as sql
from sqlite3 import Error
import os
import json
import requests

db = 'db/hack.db'

def create_connection(db):
  conn = None
  try:
    conn = sql.connect(db)
    print('DB Connected')
  except Error as e:
    print('Error:',e)
  return conn

def process_files():
  for file in os.listdir('json-files/'):
    process_file(file)

def process_file(file):
  file = 'json-files/AC2-07337-anon.json'
  data = json.load(open(file))
  add_to_db(data, file)

def add_to_db(data, file):
  conn = create_connection(db)
  elements = ['Index', 'WorkOrder', 'PartNumber', 'PartDescription', 'ToolLocation', 'Comment1', 'Comment2', 'Comment3', 'PartTCs', 'PartProbes', 'OtherSensors']
  x = data['PartInformation']
  for part_info in x:
    # tmp = part_info['PartTCs']
    for i in range(8, 11):
      # print(i)
      str = elements[i]
      part_info[str] = ', '.join(part_info[str])
      # print(part_info[str], end='\n\n')
    l=[]
    for element in elements:
      l.append(part_info[element])
    l.append(file)
    add_part_info(conn, l)

  elements = ['FileName', 'FilePath', 'LoadNumber', 'Equipment', 'RunRecipe', 'RunStart', 'RunEnd', 'RunDuration', 'OperatorName', 'ExportControl']
  x = data['RunDetails']
  l=[]
  for element in elements:
    l.append(x[element])
  l.append(file)
  add_run_detail(conn, l)

def add_run_detail(conn, l):
  query = ''' INSERT INTO RunDetails(FileName,FilePath,LoadNumber,Equipment,RunRecipe,RunStart,RunEnd,RunDuration,OperatorName,ExportControl,EntryName)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
  c = conn.cursor()
  c.execute(query, l)
  print('Added Run Detail')
  conn.commit()

def add_part_info(conn, l):
  query = ''' INSERT INTO PartInformation(`Index`,WorkOrder,PartNumber,PartDescription,ToolLocation,Comment1,Comment2,Comment3,PartTCs,PartProbes,OtherSensors,EntryName)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
  c = conn.cursor()
  print(l)
  c.execute(query, l)
  print('Added Part Information')
  conn.commit()

def main():
  # if conn:
  #   pass
  # else:
  #   print('DB connection failed')
  process_files()

if __name__ == '__main__':
  main()