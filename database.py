from flask import Flask, render_template, send_from_directory, g, jsonify
from sqlalchemy import Column, String, Sequence, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship
import sqlite3
import logging
import csv, json
from csv_reader import read_csv
from utils import dump_data

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
    constituencies = relationship('Constituency')

    @property
    def serializable(self):
        return{
            'id': self.id,
            'name': self.name,
            'belongs_to': self.belongs_to,
            'constituencies': self.constituencies
        }

class Constituency(Base):
    __tablename__ = 'constituencies'    
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String)
    belongs_to = Column(Integer, ForeignKey('states.id'))
    state = relationship('State')
    parties = relationship('Party')

    @property
    def serializable(self):
        return{
            'id': self.id,
            'belongs_to': self.belongs_to,
            'results': self.parties
        }

class Party(Base):
    __tablename__ = 'parties'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String)        
    votes = relationship("Vote")
    votes = relationship('Constituency')

    @property
    def serializable(self):
        return{
            'id': self.id,
            'name': self.name,
            'constituencies_id': self.constituencies_id,
            'constituencies': self.constituencies,
            'votes': self.votes
        }
    
 
class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    first_provisionally_votes = Column(Integer)
    first_previous_votes = Column(Integer)
    second_provisionally_votes = Column(Integer)
    second_previous_votes = Column(Integer)
    party_id = Column(Integer, ForeignKey('parties.id'))
    party = relationship('Party')
    constituency_id = (Integer, ForeignKey('constituenies.id')
    constituency = relationship('constituency')

    @property
    def serializable(self):
        return{
        'id': self.id,
        'provisionally_votes': self.provisionally_votes,
        'previouse_votes': self.prevous_votes,
        'party': self.party
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
                d = State(id = id, name = name)
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
                    
                votes = Vote(party_id = party.id,constituency_id = belongs_to , first_provisionally_votes = i.get('first').get('provisional'), first_previous_votes = i.get('first').get('previous'), second_provisionally_votes = i.get('second').get('provisional'), second_previous_votes = i.get('second').get('previous')) 
                session.add(votes)
                session.commit()
                session.flush()

def get_party_by_name(name):
        party = session.query(Party).filter(Party.name).first()
        return json.dumps(party)
    
def get_states():
        states = session.query(State.id, State.name).all()
        return json.dumps(states.serializable) 

def get_constituencies(state_id):
        constituencies = session.query(Constituency.id, Constituency.name).filter_by(state_id = state_id).all()
        return json.dumps(constituencies.serializable)

def get_db():
    if not hasattr(g, 'sqlight_db'):
        con = sqlite3.connect('btw17.db')
        g.sqlite_db = con
    return g.sqlite_db        


@app.teardown_appcontext
def close_db():
     if hasattr(g, 'sqlight_db'): g.sqlite.db.close()

addData()
app.run(debug=True)
