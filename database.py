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
cur.execute("CREATE TABLE btw17 (Nr, Gebiet, gehört_zu, Wahlberechtigte_Erststimmen, Wahlberechtigte_Zweitstimmen, Wähler_Erststimmen, Wähler_Zweitstimmen, Ungültige_Erststimmen, Ungültige_Zweitstimmen, Gültige_Erststimmen, Gültige_Zweitstimmen, Christlich_Demokratische_Union_Deutschlands_Erststimmen, Christlich_Demokratische_Union_Deutschlands_Zweitstimmen, Sozialdemokratische_Partei_Deutschlands_Erststimmen, Sozialdemokratische_Partei_Deutschlands_Zweitstimmen, DIE_LINKE_Erststimmen, DIE_LINKE_Zweitstimmen, BÜNDNIS_90_DIE_GRÜNEN_Erststimmen, BÜNDNIS_90_DIE_GRÜNEN_Zweitstimmen, Christlich_Soziale_Union_in_Bayern_e_V_Erststimmen, Christlich_Soziale_Union_in_Bayern_e_V_Zweitstimmen, Freie_Demokratische_Partei_Erststimmen, Freie_Demokratische_Partei_Zweitstimmen, Alternative_für_Deutschland_Erststimmen, Alternative_für_Deutschland_Zweitstimmen, Piratenpartei_Deutschland_Erststimmen, Piratenpartei_Deutschland_Zweitstimmen, Nationaldemokratische_Partei_Deutschlands_Erststimmen, Nationaldemokratische_Partei_Deutschlands_Zweitstimmen,FREIE_WÄHLER_Erststimmen, FREIE_WÄHLER_Zweitstimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Erststimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Zweitstimmen, Ökologisch_Demokratische_Partei_Erststimmen, Ökologisch_Demokratische_Partei_Zweitstimmen, Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Erststimmen, Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Zweitstimmen, Bayernpartei_Erststimmen, Bayernpartei_Zweitstimmen, Ab_jetzt_Demokratie_durch_Volksabstimmung_Erststimmen, Ab_jetzt_Demokratie_durch_Volksabstimmung_Zweitstimmen, Partei_der_Vernunft_Erststimmen, Partei_der_Vernunft_Zweitstimmen, Marxistisch_Leninistische_Partei_Deutschlands_Erststimmen, Marxistisch_Leninistische_Partei_Deutschlands_Zweitstimmen, Bürgerrechtsbewegung_Solidarität_Erststimmen, Bürgerrechtsbewegung_Solidarität_Zweitstimmen, Sozialistische_Gleichheitspartei_Erststimmen, Sozialistische_Gleichheitspartei_Zweitstimmen, Vierte_Internationale_Erststimmen, Vierte_Internationale_Zweitstimmen, DIE_RECHTE_Erststimmen, DIE_RECHTE_Zweitstimmen, Allianz_Deutscher_Demokraten_Erststimmen, Allianz_Deutscher_Demokraten_Zweitstimmen, Allianz_für_Menschenrechte_Erststimmen, Allianz_für_Menschenrechte_Zweitstimmen, Tier_und_Naturschutz_bergpartei_Erststimmen, Tier_und_Naturschutz_bergpartei_Zweitstimmen, die_überpartei_Erststimmen, die_überpartei_Zweitstimmen, Bündnis_Grundeinkommen_Erststimmen, Bündnis_Grundeinkommen_Zweitstimmen, DEMOKRATIE_IN_BEWEGUNG_Erststimmen, DEMOKRATIE_IN_BEWEGUNG_Zweitstimmen, Deutsche_Kommunistische_Partei_Erststimmen, Deutsche_Kommunistische_Partei_Zweitstimmen, Deutsche_Mitte_Erststimmen, Deutsche_Mitte_Zweitstimmen, Die_Grauen_–_Für_alle_Generationen_Erststimmen, Die_Grauen_–_Für_alle_Generationen_Zweitstimmen, Die_Urbane_Eine_HipHop_Partei_Erststimmen, Die_Urbane_Eine_HipHop_Partei_Zweitstimmen, Madgeburger_Gartenpartei_Erststimmen, Madgeburger_Gartenpartei_Zweitstimmen, Menschliche_Welt_Erststimmen, Menschliche_Welt_Zweitstimmen, Partei_der_Humanisten_Erststimmen, Partei_der_Humanisten_Zweitstimmen,Die_Grauen_Für_alle_Generationen_Erststimmen, Die_Grauen_Für_alle_Generationen_Zweitstimmen, Partei_für_Gesundheitsforschung_Erststimmen, Partei_für_Gesundheitsforschung_Zweitstimmen, V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Erststimmen, V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Zweitstimmen, Bündnis_C_Christen_für_Deutschland_Erststimmen, Bündnis_C_Christen_für_Deutschland_Zweitstimmen, DIE_EINHEIT_Erststimmen, DIE_EINHEIT_Zweitstimmen, Die_Violetten_Erststimmen, Die_Violetten_Zweitstimmen, Familien_Partei_Deutschlands_Erststimmen, Familien_Partei_Deutschlands_Zweitstimmen, Feministische_Partei_DIE_FRAUEN_Erststimmen, Feministische_Partei_DIE_FRAUEN_Zweitstimmen, Mieterpartei_Erststimmen, Mieterpartei_Zweitstimmen, Neue_Liberale_Die_Sozialliberalen_Erststimmen, Neue_Liberale_Die_Sozialliberalen_Zweitstimmen, UNABHÄNGIGE_für_bürgernahe_Demokratie);")
with open('btw17/btw17_kerg_modified.csv','rt', encoding = 'utf-8') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Nr'], i['Gebiet'], i['gehört_zu'], i['Wahlberechtigte_Erststimmen'],  i['Wahlberechtigte_Zweitstimmen'], i['Wähler_Erststimmen'], i['Wähler_Zweitstimmen'], i['Ungültige_Erststimmen'], i['Ungültige_Zweitstimmen'], i['Gültige_Erststimmen'], i['Gültige_Zweitstimmen'], i['Christlich_Demokratische_Union_Deutschlands_Erststimmen'], i['Christlich_Demokratische_Union_Deutschlands_Zweitstimmen'], i['Sozialdemokratische_Partei_Deutschlands_Erststimmen'], i['Sozialdemokratische_Partei_Deutschlands_Zweitstimmen'], i['DIE_LINKE_Erststimmen'], i['DIE_LINKE_Zweitstimmen'], i['BÜNDNIS_90_DIE_GRÜNEN_Erststimmen'], i['BÜNDNIS_90_DIE_GRÜNEN_Zweitstimmen'], i['Christlich_Soziale_Union_in_Bayern_e_V_Erststimmen'], i['Christlich_Soziale_Union_in_Bayern_e_V_Zweitstimmen'], i['Freie_Demokratische_Partei_Erststimmen'], i['Freie_Demokratische_Partei_Zweitstimmen'], i['Alternative_für_Deutschland_Erststimmen'], i['Alternative_für_Deutschland_Zweitstimmen'], i['Piratenpartei_Deutschland_Erststimmen'], i['Piratenpartei_Deutschland_Zweitstimmen'], i['Nationaldemokratische_Partei_Deutschlands_Erststimmen'], i['Nationaldemokratische_Partei_Deutschlands_Zweitstimmen'], i['FREIE_WÄHLER_Erststimmen'], i['FREIE_WÄHLER_Zweitstimmen'], i['PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Erststimmen'], i['PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Zweitstimmen'], i['Ökologisch_Demokratische_Partei_Erststimmen'], i['Ökologisch_Demokratische_Partei_Zweitstimmen'], i['Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Erststimmen'], i['Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Zweitstimmen'], i['Bayernpartei_Erststimmen'], i['Bayernpartei_Zweitstimmen'], i['Ab_jetzt_Demokratie_durch_Volksabstimmung_Erststimmen'], i['Ab_jetzt_Demokratie_durch_Volksabstimmung_Zweitstimmen'], i['Partei_der_Vernunft_Erststimmen'], i['Partei_der_Vernunft_Zweitstimmen'], i['Marxistisch_Leninistische_Partei_Deutschlands_Erststimmen'], i['Marxistisch_Leninistische_Partei_Deutschlands_Zweitstimmen'], i['Bürgerrechtsbewegung_Solidarität_Erststimmen'], i['Bürgerrechtsbewegung_Solidarität_Zweitstimmen'], i['Sozialistische_Gleichheitspartei_Erststimmen'], i['Sozialistische_Gleichheitspartei_Zweitstimmen'], i['Vierte_Internationale_Erststimmen'], i['Vierte_Internationale_Zweitstimmen'], i['DIE_RECHTE_Erststimmen'], i['DIE_RECHTE_Zweitstimmen'], i['Allianz_Deutscher_Demokraten_Erststimmen'], i['Allianz_Deutscher_Demokraten_Zweitstimmen'], i['Allianz_für_Menschenrechte_Erststimmen'], i['Allianz_für_Menschenrechte_Zweitstimmen'], i['Tier_und_Naturschutz_bergpartei_Erststimmen'], i['Tier_und_Naturschutz_bergpartei_Zweitstimmen'], i['die_überpartei_Erststimmen'], i['die_überpartei_Zweitstimmen'], i['Bündnis_Grundeinkommen_Erststimmen'], i['Bündnis_Grundeinkommen_Zweitstimmen'], i['DEMOKRATIE_IN_BEWEGUNG_Erststimmen'], i['DEMOKRATIE_IN_BEWEGUNG_Zweitstimmen'], i['Deutsche_Kommunistische_Partei_Erststimmen'], i['Deutsche_Kommunistische_Partei_Zweitstimmen'], i['Deutsche_Mitte_Erststimmen'], i['Deutsche_Mitte_Zweitstimmen'], i['Die_Grauen_Für_alle_Generationen_Erststimmen'], i['Die_Grauen_Für_alle_Generationen_Zweitstimmen'], i['Die_Urbane_Eine_HipHop_Partei_Erststimmen'], i['Die_Urbane_Eine_HipHop_Partei_Zweitstimmen'], i['Madgeburger_Gartenpartei_Erststimmen'], i['Madgeburger_Gartenpartei_Zweitstimmen'], i['Menschliche_Welt_Erststimmen'], i['Menschliche_Welt_Zweitstimmen'], i['Partei_der_Humanisten_Erststimmen'], i['Partei_der_Humanisten_Zweitstimmen'], i['Partei_für_Gesundheitsforschung_Erststimmen'], i['Partei_für_Gesundheitsforschung_Zweitstimmen'], i['V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Erststimmen'], i['V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Zweitstimmen'] , i['Bündnis_C_Christen_für_Deutschland_Erststimmen'], i['Bündnis_C_Christen_für_Deutschland_Zweitstimmen'], i['DIE_EINHEIT_Erststimmen'], i['DIE_EINHEIT_Zweitstimmen'], i['Die_Violetten_Erststimmen'], i['Die_Violetten_Zweitstimmen'], i['Familien_Partei_Deutschlands_Erststimmen'], i['Familien_Partei_Deutschlands_Zweitstimmen'], i['Feministische_Partei_DIE_FRAUEN_Erststimmen'], i['Feministische_Partei_DIE_FRAUEN_Zweitstimmen'], i['Mieterpartei_Erststimmen'], i['Mieterpartei_Zweitstimmen'], i['Neue_Liberale_Die_Sozialliberalen_Erststimmen'], i['Neue_Liberale_Die_Sozialliberalen_Zweitstimmen'], i['UNABHÄNGIGE_für_bürgernahe_Demokratie']) for i in dr]
cur.executemany("INSERT INTO btw17 (Nr, Gebiet, gehört_zu, Wahlberechtigte_Erststimmen, Wahlberechtigte_Zweitstimmen, Wähler_Erststimmen, Wähler_Zweitstimmen, Ungültige_Erststimmen, Ungültige_Zweitstimmen, Gültige_Erststimmen, Gültige_Zweitstimmen, Christlich_Demokratische_Union_Deutschlands_Erststimmen, Christlich_Demokratische_Union_Deutschlands_Zweitstimmen, Sozialdemokratische_Partei_Deutschlands_Erststimmen, Sozialdemokratische_Partei_Deutschlands_Zweitstimmen, DIE_LINKE_Erststimmen, DIE_LINKE_Zweitstimmen, BÜNDNIS_90_DIE_GRÜNEN_Erststimmen, BÜNDNIS_90_DIE_GRÜNEN_Zweitstimmen, Christlich_Soziale_Union_in_Bayern_e_V_Erststimmen, Christlich_Soziale_Union_in_Bayern_e_V_Zweitstimmen, Freie_Demokratische_Partei_Erststimmen, Freie_Demokratische_Partei_Zweitstimmen, Alternative_für_Deutschland_Erststimmen, Alternative_für_Deutschland_Zweitstimmen, Piratenpartei_Deutschland_Erststimmen, Piratenpartei_Deutschland_Zweitstimmen, Nationaldemokratische_Partei_Deutschlands_Erststimmen, Nationaldemokratische_Partei_Deutschlands_Zweitstimmen, FREIE_WÄHLER_Erststimmen, FREIE_WÄHLER_Zweitstimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Erststimmen, PARTEI_MENSCH_UMWELT_TIERSCHUTZ_Zweitstimmen, Ökologisch_Demokratische_Partei_Erststimmen, Ökologisch_Demokratische_Partei_Zweitstimmen, Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Erststimmen, Partei_für_Arbeit_Rechtsstaat_Tierschutz_Elitenförderung_und_basisdemokratische_Initiative_Zweitstimmen, Bayernpartei_Erststimmen, Bayernpartei_Zweitstimmen, Ab_jetzt_Demokratie_durch_Volksabstimmung_Erststimmen, Ab_jetzt_Demokratie_durch_Volksabstimmung_Zweitstimmen, Partei_der_Vernunft_Erststimmen, Partei_der_Vernunft_Zweitstimmen, Marxistisch_Leninistische_Partei_Deutschlands_Erststimmen, Marxistisch_Leninistische_Partei_Deutschlands_Zweitstimmen, Bürgerrechtsbewegung_Solidarität_Erststimmen, Bürgerrechtsbewegung_Solidarität_Zweitstimmen, Sozialistische_Gleichheitspartei_Erststimmen, Sozialistische_Gleichheitspartei_Zweitstimmen, Vierte_Internationale_Erststimmen, Vierte_Internationale_Zweitstimmen, DIE_RECHTE_Erststimmen, DIE_RECHTE_Zweitstimmen, Allianz_Deutscher_Demokraten_Erststimmen, Allianz_Deutscher_Demokraten_Zweitstimmen, Allianz_für_Menschenrechte_Erststimmen, Allianz_für_Menschenrechte_Zweitstimmen, Tier_und_Naturschutz_bergpartei_Erststimmen, Tier_und_Naturschutz_bergpartei_Zweitstimmen, die_überpartei_Erststimmen, die_überpartei_Zweitstimmen, Bündnis_Grundeinkommen_Erststimmen, Bündnis_Grundeinkommen_Zweitstimmen, DEMOKRATIE_IN_BEWEGUNG_Erststimmen, DEMOKRATIE_IN_BEWEGUNG_Zweitstimmen, Deutsche_Kommunistische_Partei_Erststimmen, Deutsche_Kommunistische_Partei_Zweitstimmen, Deutsche_Mitte_Erststimmen, Deutsche_Mitte_Zweitstimmen, Die_Grauen_Für_alle_Generationen_Erststimmen, Die_Grauen_Für_alle_Generationen_Zweitstimmen, Die_Urbane_Eine_HipHop_Partei_Erststimmen, Die_Urbane_Eine_HipHop_Partei_Zweitstimmen, Madgeburger_Gartenpartei_Erststimmen, Madgeburger_Gartenpartei_Zweitstimmen, Menschliche_Welt_Erststimmen, Menschliche_Welt_Zweitstimmen, Partei_der_Humanisten_Erststimmen, Partei_der_Humanisten_Zweitstimmen, Partei_für_Gesundheitsforschung_Erststimmen, Partei_für_Gesundheitsforschung_Zweitstimmen, V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Erststimmen,V_Partei3_Partei_für_Veränderung_Vegetarier_und_Veganer_Zweitstimmen , Bündnis_C_Christen_für_Deutschland_Erststimmen, Bündnis_C_Christen_für_Deutschland_Zweitstimmen, DIE_EINHEIT_Erststimmen, DIE_EINHEIT_Zweitstimmen, Die_Violetten_Erststimmen, Die_Violetten_Zweitstimmen, Familien_Partei_Deutschlands_Erststimmen, Familien_Partei_Deutschlands_Zweitstimmen, Feministische_Partei_DIE_FRAUEN_Erststimmen, Feministische_Partei_DIE_FRAUEN_Zweitstimmen, Mieterpartei_Erststimmen, Mieterpartei_Zweitstimmen, Neue_Liberale_Die_Sozialliberalen_Erststimmen, Neue_Liberale_Die_Sozialliberalen_Zweitstimmen, UNABHÄNGIGE_für_bürgernahe_Demokratie) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,? , ?, ?, ?, ?, ?);", to_db)
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

#app.run(debug=True)
