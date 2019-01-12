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


app = Flask(__name__)


Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True, nullable = False)
    belongs_to = Column(Integer)
    leftover = Column(Integer)
    number = Column(Integer)
    constituencies = relationship('Constituency')

class Constituency(Base):
    __tablename__ = 'constituencies'    
    id = Column(Integer, primary_key = True, nullable = False)
    number = Column(Integer)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State')
    parties = relationship('Party')

class Party(Base):
    __tablename__ = 'parties'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String)
    constituency_id = Column(Integer, ForeignKey('constituencies.id'))
    constituency = relationship('Constituency')
    votes = relationship("Votes")
 
class Votes(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    provisionallyVotes = Column(Integer)
    party_id = Column(Integer, ForeignKey('parties.id'))
    party = relationship('Party')

Base.metadata.Base.create_engine(engine)
    
def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('whalkreis.db')#typo?

  g.sqlite_db = con
 return g.sqlite_db

@app.teardown_appcontext
def close_db (error):
  if hasattr (g, 'sqlite_db'):g.sqlite_db.close ()

app.run(debug = True)