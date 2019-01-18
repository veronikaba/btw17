from flask import Flask, render_template, send_from_directory, g, jsonify
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship
import sqlite3
import logging

Base = declarative_base()
engine = create_engine('sqlite:///btw17.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
app = Flask(__name__)


class Btw(Base):
    __table__ = Table('btw', Base.metadata,
                    autoload=True, autoload_with=engine)



   

Base.metadata.create_all(engine)


@app.route('/')
def say_hello():
    return send_from_directory("templates", "hello.html")

def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('btw17.db')
  g.sqlite_db = con
 return g.sqlite_db

#def query_db():

@app.route('/number', methods=['GET'])
def get_states():
    number = session.query(Btw).all()
    return jsonify(number)
    

@app.teardown_appcontext
def close_db (error):
  if hasattr (g, 'sqlite_db'):g.sqlite_db.close ()

app.run(debug=True)
