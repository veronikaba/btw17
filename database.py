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
    id = Column(Integer, primary_key = True, nullable = False)
    #number = Column(Integer)
    name = Column(String)
    belongs_to = Column(Integer)  
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
    #number = Column(Integer)
    belongs_to = Column(Integer)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State')
    party_id = relationship(Integer, ForeignKey('party.id'))
    parties = relationship('Party')

    @property
    def serializable(self):
        return{
            'id': self.id,
            'belongs_to': self.belongs_to,
            'state_id': self.state_id,
            'state': self.state,
            'party_id': self.party_id,
            'parties': self.parties
        }

class Parties(Base):
    __tablename__ = 'parties'
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String)
    constituency_id = Column(Integer, ForeignKey('constituencies.id'))
    constituency = relationship('Constituency')
    votes = relationship("Votes")

    @property
    def serializable(self):
        return{
            'id': self.id,
            'name': self.name,
            'constituency_id': self.constituency_id,
            'constituency': self.constituency,
            'votes': self.votes
        }
    
 
class Votes(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    first_provisionally_votes = Column(Integer)
    first_previous_votes = Column(Integer)
    second_provisionally_votes = Column(Integer)
    second_previous_votes = Column(Integer)
    party_id = Column(Integer, ForeignKey('parties.id'))
    party = relationship('Party')

    @property
    def serializable(self):
        return{
        'id': self.id,
        'provisionally_votes': self.provisionally_votes,
        'previouse_votes': self.prevous_votes,
        'party_id': self.party_id,
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

            if belongs_to != 99:
                d = Constituency( id = id, name = name, belongs_to = belongs_to)
            else:
                d = State(id = id, name = name)
            
            for i in d.results:
                party = get_party_by_name(i.get('name'))
                if party != []:
                    party_id =party.id
                else:
                     party = Parties(name = party.name)
                     session.add(party)
                     session.commit()
                     session.flush()
                     party_id = party.id
                    
                votes = Votes (party_id = party.id, first_provisionally_votes = i.get('first').get('provisional'), first_prevoius_votes = i.get('first').get('previous'), second_provisionally_votes = i.get('second').get('provisional'), second_previous_votes = i.get('second'.get('previous')) )
                session.add(votes)
                session.commit()
                session.flush()

def get_party_by_name(name):
        party = session.query(Parties).filter(Parties.name).first()
        return party
    


def get_db():
    if not hasattr(g, 'sqlight_db'):
        con = sqlite3.connect('btw17.db')
        g.sqlite_db = con
    return g.sqlite_db        


@app.teardown_appcontext
def close_db():
     if hasattr(g, 'sqlight_db'): g.sqlite.db.close()


app.run(debug=True)
