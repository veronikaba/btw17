from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String
from flask import Flask
from flask import render_template
from flask import g
from numpy import genfromtxt
import csv
import logging
import sqlite3

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',')
    return data.tolist

Base = declarative_base()
engine = create_engine('sqlite:///btw17.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine, autocommit = True)
session = Session()
app = Flask(__name__)

con = sqlite3.connect('btw17.db')
cur = con.cursor()
cur.execute("CREATE TABLE btw17 (Nr, Gebiet, gehoert_zu, Wahlberechtigte, Wähler);")
with open('btw17_kerg_modify.csv','rt', encoding = 'utf-8') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Nr'], i['Gebiet'], i['gehoert_zu'], i['Wahlberechtigte'],  i['Wähler']) for i in dr if i[0] != ""]
cur.executemany("INSERT INTO btw17 (Nr, Gebiet, gehoert_zu, Wahlberechtigte, Wähler) VALUES (?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('btw17.db')
  cur = con.cursor()
  g.sqlite_db = con
 return g.sqlite_db

@app.teardown_appcontext
def close_db (error):
  if hasattr (g, 'sqlite_db'):g.sqlite_db.close ()

app.run(debug = True)
