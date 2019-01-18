from flask import Flask, render_template, send_from_directory, g, jsonify
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship
import sqlite3
import logging
import csv, json

Base = declarative_base()
engine = create_engine('sqlite:///btw17.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
app = Flask(__name__)


#class Btw(Base):
#    __table__ = Table('btw', Base.metadata,
#                    autoload=True, autoload_with=engine)

class Btw(Base):
    __tablename__ = 'btw17'
    Gebiet = Column(String, primary_key=True)
    
   


@app.route('/')
def say_hello():
    return send_from_directory("templates", "hello.html")

def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('btw17.db')
  g.sqlite_db = con
 return g.sqlite_db

#def query_db():
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
  
@app.route('/number', methods=['GET'])
def get_states():
    number = session.query(Btw).all()
    logging.error(number)
    return json.dumps(number, cls=AlchemyEncoder)
    

@app.teardown_appcontext
def close_db (error):
  if hasattr (g, 'sqlite_db'):g.sqlite_db.close ()

app.run(debug=True)
