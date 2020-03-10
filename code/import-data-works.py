import csv
import sys
import json
import sqlite3



COLUMNS    = ['type','key','revision','last_modified','json']
INPUT_FILE = 'data/small_works.txt'
#INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
#DB_FILE = 'opendata.db'
#DB_FILE = 'databases.db'
DB_FILE = 'bdd/databases.db'
#DB_FILE = ":memory:"
DB_SCHEMA = 'sql/schema-works.sql'


db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript(open(DB_SCHEMA,'r').read())

for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
     j = json.loads(record['json'])
     #print(record['key'],j['key'],record['key'] == j['key'],j.get('name'),j.get('birth_date'),j.get('death_date'),j.get('title'),j.get('bio'))
     #c.execute('INSERT INTO AUTHOR VALUES (?,?,?)',[record['key'],j['name'],j.get('birth_date')])
     c.execute('INSERT INTO WORKS VALUES (?,?,?,?,?,?,?)',[record['key'],j.get('title'),j.get('subtitle'),j.get('first_sentence'),j.get('first_publish_date'),j.get('notes'),j.get('cover_edition')])
db.commit()
db.close()