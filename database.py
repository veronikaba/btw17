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
cur.execute("CREATE TABLE btw17 (Nr, Gebiet, gehoert_zu, Wahlberechtigte_Erststimmen, Wahlberechtigte_Zweitstimmen, Wähler_Erststimmen, Wähler_Zweitstimmen, Ungültige_Erststimmen, Ungültige_Zweitstimmen, Gültige_Erststimmen, Gültige_Zweitstimmen, Christlich_Demokratische_Union_Deutschlands_Erststimmen, Christlich_Demokratische_Union_Deutschlands_Zweitstimmen, Sozialdemokratische_Partei_Deutschlands_Erststimmen, Sozialdemokratische_Partei_Deutschlands_Zweitstimmen, DIE_LINKE_Erststimmen, DIE_LINKE_Zweitstimmen, BÜNDNIS_90/DIE_GRÜNEN_Erststimmen, BÜNDNIS_90/DIE_GRÜNEN_Zweitstimmen, Christlich-Soziale_Union_in_Bayern_e.V._Erststimmen, Christlich-Soziale_Union_in_Bayern_e.V._Zweitstimmen, Freie_Demokratische_Partei_Erststimmen, Freie_Demokratische_Partei_Zweitstimmen, Alternative_für_Deutschland_Erststimmen, Alternative_für_Deutschland_Zweitstimmen, Piratenpartei_Deutschland_Erststimmen, Piratenpartei_Deutschland_Zweitstimmen, Nationaldemokratische_Partei_Deutschlands_Erststimmen, Nationaldemokratische_Partei_Deutschlands_Zweitstimmen, FREIE_WÄHLER_Zeritstimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Erststimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Zweitstimmen, Ökologisch-Demokratische_Partei_Erststimmen, Ökologisch-Demokratische_Partei_Zweitstimmen, Partei_für_Arbeit,_Rechtsstaat,_Tierschutz,_Elitenförderung_und_basisdemokratische_Initiative_Erststimmen, Partei_für_Arbeit,_Rechtsstaat,_Tierschutz,_Elitenförderung_und_basisdemokratische_Initiative_Zweitstimmen, Bayernpartei_Erststimmen, Bayernpartei_Zweitstimmen);")
with open('btw17_kerg_modified.csv','rt', encoding = 'utf-8') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Nr'], i['Gebiet'], i['gehoert_zu'], i['Wahlberechtigte_Erststimmen'],  i['Wahlberechtigte_Zweitstimmen'], i['Wähler_Erststimmen'], i['Wähler_Zweitstimmen'], i['Ungültige_Erststimmen'], i['Ungültige_Zweitstimmen'], i['Gültige_Erststimmen'], i['Gültige_Zweitstimmen'], i['Christlich_Demokratische_Union_Deutschlands_Erststimmen'], i['Christlich_Demokratische_Union_Deutschlands_Zweitstimmen'], i['Sozialdemokratische_Partei_Deutschlands_Erststimmen'], i['Sozialdemokratische_Partei_Deutschlands_Zweitstimmen'], i['DIE_LINKE_Erststimmen'], i[' DIE_LINKE_Zweitstimmen'], i['BÜNDNIS_90/DIE_GRÜNEN_Erststimmen'], i['BÜNDNIS_90/DIE_GRÜNEN_Zweitstimmen'], i['Christlich-Soziale_Union_in_Bayern_e.V._Erststimmen'], i['Christlich-Soziale_Union_in_Bayern e.V._Zweitstimmen'], i['Freie_Demokratische_Partei_Erststimmen'], i['Freie_Demokratische_Partei_Zweitstimmen'], i['Alternative_für_Deutschland_Erststimmen'], i['Alternative_für_Deutschland_Zweitstimmen'], i['Piratenpartei_Deutschland_Erststimmen'], i['Piratenpartei_Deutschland_Zweitstimmen'], i['Nationaldemokratische_Partei_Deutschlands_Erststimmen'], i['Nationaldemokratische_Partei_Deutschlands_Zweitstimmen'], i['FREIE_WÄHLER_Erststimmen'], i['FREIE_WÄHLER_Zweitstimmen'], i['PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Erststimmen'], i['PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Zweitstimmen'], i['Ökologisch-Demokratische_Partei_Erststimmen'], i['Ökologisch-Demokratische_Partei_Zweitstimmen'], i['Partei_für_Arbeit,_Rechtsstaat,_Tierschutz,_Elitenförderung_und_basisdemokratische_Initiative_Erststimmen'], i['Partei_für_Arbeit,_Rechtsstaat,_Tierschutz,_Elitenförderung_und_basisdemokratische_Initiative_Zweitstimmen'], i['Bayernpartei_Erststimmen'], i['Bayernpartei_Zweitstimmen']) for i in dr]
cur.executemany("INSERT INTO btw17 (Nr, Gebiet, gehoert_zu, Wahlberechtigte_Erststimmen, Wahlberechtigte_Zweitstimmen, Wähler_Erststimmen, Wähler_Zweitstimmen, Ungültige_Erststimmen, Ungültige_Zweitstimmen, Gültige_Erststimmen, Gültige_Zweitstimmen, Christlich_Demokratische_Union_Deutschlands_Erststimmen, Christlich_Demokratische_Union_Deutschlands_Zweitstimmen, Sozialdemokratische_Partei_Deutschlands_Erststimmen, Sozialdemokratische_Partei_Deutschlands_Zweitstimmen, DIE_LINKE_Erststimmen, DIE_LINKE_Zweitstimmen, BÜNDNIS_90/DIE_GRÜNEN_Erststimmen, BÜNDNIS_90/DIE GRÜNEN_Zweitstimmen, Christlich-Soziale_Union_in_Bayern e.V._Erststimmen, Christlich-Soziale_Union_in_Bayern_e.V._Zweitstimmen, Freie_Demokratische_Partei_Erststimmen, Freie_Demokratische_Partei_Zweitstimmen, Alternative_für_Deutschland_Erststimmen, Alternative_für_Deutschland_Zweitstimmen, Piratenpartei_Deutschland_Erststimmen, Piratenpartei_Deutschland_Zweitstimmen, Nationaldemokratische_Partei_Deutschlands_Erststimmen, Nationaldemokratische_Partei_Deutschlands_Zweitstimmen, FREIE_WÄHLER_Erststimmen, FREIE_WÄHLER_Zweitstimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Erststimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Zweitstimmen, Ökologisch-Demokratische_Partei_Erststimmen, Ökologisch-Demokratische_Partei_Zweitstimmen, Partei_für_Arbeit,_Rechtsstaat,_Tierschutz,_Elitenförderung_und_basisdemokratische_Initiative_Erststimmen, Partei_für_Arbeit,_Rechtsstaat,_Tierschutz,_Elitenförderung_und_basisdemokratische_Initiative_Zweitstimmen, Bayernpartei_Erststimmen, Bayernpartei_Zweitstimmen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
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

app.run(debug=True)
