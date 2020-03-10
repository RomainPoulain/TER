import csv
import sys
import json
import sqlite3



COLUMNS    = ['type','key','revision','last_modified','json']
INPUT_FILE = 'data/small-authors.txt'
#INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
#DB_FILE = 'opendata.db'
#DB_FILE = 'databases.db'
DB_FILE = 'bdd/databases.db'
#DB_FILE = ":memory:"
DB_SCHEMA = 'sql/schema.sql'


db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript(open(DB_SCHEMA,'r').read())

# # keys = set()
# i = 1
# try:
#     for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
#         #print(record['type'],record['key'],record['revision'])
#         # key = record['key']
#         # if key in keys:
#         #     print("BAM",key,record)
#         #     sys.exit(1)
#         # keys.add(key)
#         i += 1
# except:
#     print(i)



for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
     j = json.loads(record['json'])
     #print(record['key'],j['key'],record['key'] == j['key'],j.get('name'),j.get('birth_date'),j.get('death_date'),j.get('title'),j.get('bio'))
     #c.execute('INSERT INTO AUTHOR VALUES (?,?,?)',[record['key'],j['name'],j.get('birth_date')])
     c.execute('INSERT INTO AUTHORS VALUES (?,?,?,?,?,?,?,?,?,?,?)',[record['key'],j.get('name'),j.get('eastern_order'),j.get('personal_name'),j.get('enumeration'),j.get('title'),j.get('location'),j.get('birth_date'),j.get('death_date'),j.get('date'),j.get('wikipedia')])
db.commit()
db.close()



for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
    j = json.loads(record['json'])
    # if 'alternate_names' in j:
    #     print("YES",j['name'])
    #     for n in j['alternate_names']:
    #         print("   ",n)
    if 'links' in j:
        print("YES",j['name'])
        for n in j['links']:
            print("   ",n)