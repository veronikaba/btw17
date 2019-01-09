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
import sqlite3


engine = create_engine('sqlite:///wahlkreise.db')
Session = sessionmaker(bind = engine, autocommit = True)
session = Session()

Base = declarative_base()

app = Flask(__name__)



class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True, nullable = False)
    belongs_to = Column(Integer)
    leftover = Column(Integer)
    number = Column(Integer)

class Constituency(Base):
    __tablename__ = 'constituencies',
    id = Column(Integer, primary_key = True, nullable = False)
    numberr = Column(Integer)
    relationship("Party")

class Party(Base):
    __tablename__ = 'parties',
    id = Column(Integer, primary_key = True, nullable = False),
    name = Column(String),
    area_id = Column(Integer, ForeignKey("constituencies.id"))
    voter = relationship("Voter") 

class Voter(Base):

    id = Column(Integer, primary_key=True)
    relationship("Votes")

class Votes(Base):
    id = Column(primary_key = True),
    provisionally = Column(Integer),
    before_period = Column(Integer)



    
def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('whalkreis.db')#typo?

  g.sqlite_db = con
 return g.sqlite_db

@app.teardown_appcontext
def close_db (error):
  if hasattr (g, 'sqlite_db'):g.sqlite_db.close ()
