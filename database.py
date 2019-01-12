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




class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True, nullable = False)
    belongs_to = Column(Integer)
    leftover = Column(Integer)
    number = Column(Integer)
    constituencies = relationship('Constituency')


#constintuency_party = Table ('constituency_parties',
#    Base.metadata,
#   Column (constituency_id,Integer, ForeignKey('parties.id')),
#   Column (party_id,Integer, ForeignKey('constituencies.id')))
 
class Constituency(Base):
    __tablename__ = 'constituencies'    
    id = Column(Integer, primary_key = True, nullable = False)
    number = Column(Integer)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State')
    parties = relationship('Party')
    belongs_to = Column(Integer)

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
    provisionally_votes = Column(Integer)
    party_id = Column(Integer, ForeignKey('parties.id'))
    party = relationship('Party')


try:
    file_name = 'btw17_kerg_modify.csv'
    data = Load_Data(file_name)

    for i in data:
        constituency = Constituency(**{
         'name' : i[1],
         'number' : i[0],
         'belongs_to' : i[2]
        })
        j = 3
        if j % 4 == 0:
            record = Party(**{
                'name' : i[i+1],
                'constituency_id' : constituency.id
             })
        session.add(record)
        session.add(constituency)
        session.commit()
except:
    session.rollback()

finally:
    session.close()
    


def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('btw17.db')
  g.sqlite_db = con
 return g.sqlite_db

@app.teardown_appcontext
def close_db (error):
  if hasattr (g, 'sqlite_db'):g.sqlite_db.close ()
app.run(debug = True)