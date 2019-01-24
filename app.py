from flask import Flask, render_template, send_from_directory, g, jsonify
from sqlalchemy import Integer, Column, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship
import sqlite3
import logging
import csv, json
from csv_reader import read_csv

Base = declarative_base()
engine = create_engine('sqlite:///btw17.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
app = Flask(__name__)


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    belongs_to = Column(Integer)
    constituencies = relationship('Constituency')

    @property
    def serializable(self):
        return{
            'id': self.id,
            'name': self.name,
            'belongs_to': self.belongs_to
        }

class Constituency(Base):
    __tablename__ = 'constituencies'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String)
    belongs_to = Column(Integer, ForeignKey('states.id'))
    state = relationship('State')
    votes = relationship('Vote')

    @property
    def serializable(self):
        return{
            'id': self.id,
            'name': self.id,
            'belongs_to': self.belongs_to
        }

class Party(Base):
    __tablename__ = 'parties'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String)        
    votes = relationship("Vote")

    @property
    def serializable(self):
        return{
            'id': self.id,
            'name': self.name
        }
    
 
class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    first_provisional_votes = Column(Integer)
    first_previous_votes = Column(Integer)
    second_provisional_votes = Column(Integer)
    second_previous_votes = Column(Integer)
    party_id = Column(Integer, ForeignKey('parties.id'))
    party = relationship('Party')
    constituency_id = Column(Integer, ForeignKey('constituencies.id'))
    constituency = relationship('Constituency')

    @property
    def serializable(self):
        return{
        'id': self.id,
        'provisionall_votes': {
            'first': self.first_provisional_votes,
            'second': self.second_provisional_votes
        },
        'previous_votes':{
            'first': self.first_previous_votes,
            'second': self.second_previous_votes
        },
        'party_id': self.party_id,
        'constituency_id': self.constituency_id
        }

Base.metadata.create_all(engine)

def addData():
        data = read_csv()
        session = Session()
        for c in data:
            id = c.get('id')
            name = c.get('name')
            belongs_to = c.get('belongs_to')
            
            if belongs_to != '99' and belongs_to != '':
                d = Constituency(id = id, name = name, belongs_to = belongs_to)
            else:
                d = State(id = id, name = name, belongs_to = '99')
            session.add(d)
            session.commit()
            session.flush
            for i in c.get('parties'):
                party = get_party_by_name(i.get('name'))
                if not party is None:
                    party_id = party.id
                else:
                    party = Party(name = name)
                    session.add(party)
                    session.commit()
                    session.flush()
                    party_id = party.id
                    
                votes = Vote(party_id = party.id,constituency_id = id , first_provisional_votes = i.get('first').get('provisional'), first_previous_votes = i.get('first').get('previous'), second_provisional_votes = i.get('second').get('provisional'), second_previous_votes = i.get('second').get('previous')) 
                session.add(votes)
                session.commit()
                session.flush()


def get_party_by_name(name):
        party = session.query(Party).filter(Party.name).first()
        return party

@app.route('/states', methods=['GET'])    
def get_states():
        states = session.query(State.name, State.id).all()
        return json.dumps(states) 

@app.route('/constituencies/<state>', methods=['GET'])
def get_constituencies(state):
        constituencies = session.query(Constituency.serializable).filter_by(state_id = state).all()
        return json.dumps(constituencies)

@app.route('/constituencies/<constituency>', methods=['GET'])
def get_votes(constituency):
        votes = session.query(Vote.serializable).filter_by(constituency_id = constituency).all()
        return json.dumps(votes)

@app.route('/')
def say_hello():
    return send_from_directory("templates", "hello.html")

def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('btw17.db', check_same_thread=False)
  g.sqlite_db = con
 return g.sqlite_db


@app.teardown_appcontext
def close_db (error):
  if hasattr (g, 'sqlite_db'):g.sqlite_db.close ()


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data).encode('utf8') # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

            
app.run(debug=True)
