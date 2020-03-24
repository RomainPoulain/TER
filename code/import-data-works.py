import csv
import sys
import json
import sqlite3

COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = '../data/small_works.txt'
# INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
# DB_FILE = 'opendata.db'
# DB_FILE = 'databases.db'
DB_FILE = '../bdd/databases.db'
# DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema-works.sql'

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript(open(DB_SCHEMA, 'r').read())

for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
    j = json.loads(record['json'])

    subjects = ''
    if 'subjects' in j:
        for n in j['subjects']:
            subjects = n
    else:
        subjects = None

    subject_places = ''
    if 'sucject_places' in j:
        for n in j['subject_places']:
            subject_places = n
    else:
        subject_places = None

    subject_times = ''
    if 'subject_times' in j:
        for n in j['subject_times']:
            subject_times = n
    else:
        subject_times = None

    subject_people = ''
    if 'subject_people' in j:
        for n in j['subject_people']:
            subject_people = n
    else:
        subject_people = None

    description = ''
    if 'description' in j and 'value' in j['description']:
        description = j['description']['value']
    else:
        description = None

    dewey_number = ''
    if 'dewey_number' in j:
        for n in j['dewey_number']:
            dewey_number = n
    else:
        dewey_number = None

    lc_classifications = ''
    if 'lc_classifications' in j:
        for n in j['lc_classifications']:
            lc_classifications = n
    else:
        lc_classifications = None

    other_titles = ''
    if 'other_titles' in j:
        for n in j['other_titles']:
            other_titles = n
    else:
        other_titles = None

    covers = ''
    if 'covers' in j:
        for n in j['covers']:
            covers = n
    else:
        covers = None

    c.execute('INSERT INTO WORKS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
              [record['key'],
               j.get('title'),
               j.get('subtitle'),
               subjects,
               subject_places,
               subject_times,
               subject_people,
               description,
               dewey_number,
               lc_classifications,
               j.get('first_sentence'),
               other_titles,
               j.get('first_publish_date'),
               j.get('notes'),
               j.get('cover_edition'),
               covers])
db.commit()

print(subjects)