from flask import Flask, render_template, send_from_directory, g, jsonify
from sqlalchemy import Integer, Column, String, Sequence
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.pool import SingletonThreadPool
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, relationship
import sqlite3
import logging
import csv, json

Base = declarative_base()
engine = create_engine('sqlite:///btw17.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
app = Flask(__name__)


class Btw(Base):
    __tablename__ = 'btw17'
    Gebiet = Column(String, primary_key = True)
    Nr = Column(Integer)
    gehört_zu = Column(Integer)
    Wahlberechtigte_Erststimmen = Column(Integer)
    Wahlberechtigte_Zweitstimmen = Column(Integer)
    Wähler_Erststimmen = Column(Integer)
    Wähler_Zweitstimmen = Column(Integer)
    Ungültige_Erststimmen = Column(Integer)
    Ungültige_Zweitstimmen = Column(Integer)
    Gültige_Erststimmen = Column(Integer)
    Gültige_Zweitstimmen = Column(Integer)
    Gültige_Erststimmen = Column(Integer)
    Christlich_Demokratische_Union_Deutschlands_Erststimmen = Column(Integer)
    Christlich_Demokratische_Union_Deutschlands_Zweitstimmen = Column(Integer)
    Sozialdemokratische_Partei_Deutschlands_Erststimmen = Column(Integer)
    Sozialdemokratische_Partei_Deutschlands_Zweitstimmen = Column(Integer)
    BÜNDNIS_90_DIE_GRÜNEN_Erststimmen = Column(Integer)
    BÜNDNIS_90_DIE_GRÜNEN_Zweitstimmen = Column(Integer)
    Christlich_Soziale_Union_in_Bayern_e_V_Erststimmen = Column(Integer)
    Christlich_Soziale_Union_in_Bayern_e_V_Zweitstimmen = Column(Integer)
    Freie_Demokratische_Partei_Erststimmen = Column(Integer)
    Freie_Demokratische_Partei_Zweitstimmen = Column(Integer)
    Alternative_für_Deutschland_Erststimmen = Column(Integer)
    Alternative_für_Deutschland_Zweitstimmen = Column(Integer)
    Piratenpartei_Deutschland_Erststimmen = Column(Integer)
    Piratenpartei_Deutschland_Zweitstimmen = Column(Integer)
    Nationaldemokratische_Partei_Deutschlands_Erststimmen = Column(Integer)
    Nationaldemokratische_Partei_Deutschlands_Zweitstimmen = Column(Integer)
    FREIE_WÄHLER_Erststimmen = Column(Integer)
    FREIE_WÄHLER_Zweitstimmen = Column(Integer)
    PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Erststimmen = Column(Integer)
    PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Zweitstimmen = Column(Integer)
    Ökologisch_Demokratische_Partei_Erststimmen = Column(Integer)
    Ökologisch_Demokratische_Partei_Zweitstimmen = Column(Integer)
    Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Erststimmen = Column(Integer)    
    Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Zweitstimmen = Column(Integer)
    Bayernpartei_Erststimmen = Column(Integer)
    Bayernpartei_Zweitstimmen = Column(Integer)
    Ab_jetzt_Demokratie_durch_Volksabstimmung_Erststimmen = Column(Integer)
    Ab_jetzt_Demokratie_durch_Volksabstimmung_Zweitstimmen = Column(Integer)
    Partei_der_Vernunft_Erststimmen = Column(Integer)
    Partei_der_Vernunft_Zweitstimmen = Column(Integer)
    Marxistisch_Leninistische_Partei_Deutschlands_Erststimmen = Column(Integer)
    Marxistisch_Leninistische_Partei_Deutschlands_ZWeitstimmen = Column(Integer)
    Bürgerrechtsbewegung_Solidarität_Erststimmen = Column(Integer)
    Bürgerrechtsbewegung_Solidarität_Zweitstimmen = Column(Integer)
    Sozialistische_Gleichheitspartei_Erststimmen = Column(Integer)
    Sozialistische_Gleichheitspartei_Zweitstimmen = Column(Integer)
    Vierte_Internationale_Erststimmen = Column(Integer)
    Vierte_Internationale_Zweitstimmen = Column(Integer)
    DIE_RECHTE_Erststimmen = Column(Integer)
    DIE_RECHTE_Zweitstimmen = Column(Integer)
    Allianz_Deutscher_Demokraten_Erststimmen = Column(Integer)
    Allianz_Deutscher_Demokraten_Zweitstimmen = Column(Integer)
    Allianz_für_Menschenrechte_Erststimmen = Column(Integer)
    Allianz_für_Menschenrechte_Zweitstimmen = Column(Integer)
    Tier_und_Naturschutz_bergpartei_Erststimmen = Column(Integer)
    Tier_und_Naturschutz_bergpartei_Zweitstimmen = Column(Integer)
    die_überpartei_Erststimmen = Column(Integer)
    die_überpartei_Zweitstimmen = Column(Integer)
    Bündnis_Grundeinkommen_Erststimmen = Column(Integer)
    Bündnis_Grundeinkommen_Zweitstimmen = Column(Integer)
    DEMOKRATIE_IN_BEWEGUNG_Erststimmen = Column(Integer)
    Deutsche_Kommunistische_Partei_Erststimmen = Column(Integer)
    Deutsche_Mitte_Erststimmen = Column(Integer)
    Deutsche_Mitte_Zweitstimmen = Column(Integer)
    Die_Grauen_Für_alle_Generationen_Erststimmen = Column(Integer)
    Die_Grauen_Für_alle_Generationen_Zweitstimmen = Column(Integer)
    Die_Urbane_Eine_HipHop_Partei_Erststimmen = Column(Integer)
    Die_Urbane_Eine_HipHop_Partei_Zweitstimmen = Column(Integer)
    Madgeburger_Gartenpartei_Erststimmen = Column(Integer)
    Madgeburger_Gartenpartei_Zweitstimmen = Column(Integer)
    Menschliche_Welt_Erststimmen = Column(Integer)
    Menschliche_Welt_Zweitstimmen = Column(Integer)
    Partei_der_Humanisten_Erststimmen = Column(Integer)
    Partei_der_Humanisten_Zweitstimmen = Column(Integer)
    Partei_für_Gesundheitsforschung_Erststimmen = Column(Integer)
    Partei_für_Gesundheitsforschung_Zweitstimmen = Column(Integer)
    V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Erststimmen = Column(Integer)
    V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Zweitstimmen = Column(Integer)
    Die_Violetten_Erststimmen = Column(Integer)
    Die_Violetten_Zweitstimmen = Column(Integer)
    Familien_Partei_Deutschlands_Erststimmen = Column(Integer)
    Familien_Partei_Deutschlands_Zweitstimmen = Column(Integer)
    Feministische_Partei_DIE_FRAUEN_Erststimmen = Column(Integer)
    Feministische_Partei_DIE_FRAUEN_Zweitstimmen = Column(Integer)
    Mieterpartei_Erststimmen = Column(Integer)
    Mieterpartei_Zweitstimmen = Column(Integer)
    Neue_Liberale_Die_Sozialliberalen_Erststimmen = Column(Integer)
    Neue_Liberale_Die_Sozialliberalen_Zweitstimmen = Column(Integer)
    UNABHÄNGIGE_für_bürgernahe_Demokratie = Column(Integer)


@app.route('/')
def say_hello():
    return send_from_directory("templates", "hello.html")

def get_db () :
 if not hasattr(g,'sqlite_db'):
  con = sqlite3.connect('btw17.db', check_same_thread=False)
  g.sqlite_db = con
 return g.sqlite_db


#def query_db():
@app.route('/all', methods=['GET'])
def get_all():
    number = session.query(Btw).all()
    return json.dumps(number, cls=AlchemyEncoder)


@app.route('/id', methods=['GET'])
def get_id():
    area = session.query(Btw).filter(Btw.gehört_zu.isnot(0)).all()
    return json.dumps(area, cls=AlchemyEncoder)    

@app.route('/area', methods=['GET'])
def get_area():
    area = session.query(Btw.Gebiet).all()
    return json.dumps(area, cls=AlchemyEncoder)

@app.route('/constituencies/const', methods=['GET'])
def get_constituencie(const):
    constituency = session.query(Btw).filter_by(Gebiet = const).first()
    return json.dumps(constituency, cls=AlchemyEncoder)

    
@app.route('/constituencies', methods=['GET'])
def get_constituencies():
    constituencies = session.query(Btw).filter(Btw.gehört_zu.isnot('99')).all()
    return json.dumps(constituencies, cls=AlchemyEncoder)

@app.route('/number', methods=['GET'])
def get_number():
    number = session.query(Btw.Nr).all()
    return json.dumps(number, cls=AlchemyEncoder)
    

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
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


app.run(debug=True)
