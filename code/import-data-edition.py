import csv
import sys
import json
import sqlite3

COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = '../data/small_edition.txt'
# INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
# DB_FILE = 'opendata.db'
# DB_FILE = 'databases.db'
DB_FILE = '../bdd/databases.db'
# DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema-edition.sql'
db = sqlite3.connect(DB_FILE)

c = db.cursor()

c.executescript(open(DB_SCHEMA, 'r').read())

for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
    j = json.loads(record['json'])

    other_titles = ''
    if 'other_titles' in j:
        for n in j['other_titles']:
            other_titles = n
    else:
        other_titles = None

    description = ''
    if 'description' in j and 'value' in j['description']:
        description = j['description']['value']
    else:
        description = None

    notes = ''
    if 'notes' in j and 'value' in j['notes']:
        notes = j['notes']['value']
    else:
        notes = None

    genres = ''
    if 'genres' in j:
        for n in j['genres']:
            genres = n
    else:
        genres = None

    work_titles = ''
    if 'work_titles' in j:
        for n in j['work_titles']:
            work_titles = n
    else:
        work_titles = None

    series = ''
    if 'series' in j:
        for n in j['series']:
            series = n
    else:
        series = None

    subjects = ''
    if 'subjects' in j:
        for n in j['subjects']:
            subjects = n
    else:
        subjects = None

    lccn = ''
    if 'lccn' in j:
        for n in j['lccn']:
            lccn = n
    else:
        lccn = None

    oclc_numbers = ''
    if 'oclc_numbers' in j:
        for n in j['oclc_numbers']:
            oclc_numbers = n
    else:
        oclc_numbers = None

    isbn_10 = ''
    if 'isbn_10' in j:
        for n in j['isbn_10']:
            isbn_10 = n
    else:
        isbn_10 = None

    isbn_13 = ''
    if 'isbn_13' in j:
        for n in j['isbn_13']:
            isbn_13 = n
    else:
        isbn_13 = None

    dewey_decimal_class = ''
    if 'dewey_decimal_class' in j:
        for n in j['dewey_decimal_class']:
            dewey_decimal_class = n
    else:
        dewey_decimal_class = None

    lc_classifications = ''
    if 'lc_classifications' in j:
        for n in j['lc_classifications']:
            lc_classifications = n
    else:
        lc_classifications = None

    contributions = ''
    if 'contributions' in j:
        for n in j['contributions']:
            contributions = n
    else:
        contributions = None

    publish_places = ''
    if 'publish_places' in j:
        for n in j['publish_places']:
            publish_places = n
    else:
        publish_places = None

    publishers = ''
    if 'publishers' in j:
        for n in j['publishers']:
            publishers = n
    else:
        publishers = None

    distributors = ''
    if 'distributors' in j:
        for n in j['distributors']:
            distributors = n
    else:
        distributors = None

    location = ''
    if 'location' in j:
        for n in j['location']:
            location = n
    else:
        location = None

    uris = ""
    if 'uris' in j:
        for n in j['uris']:
            uris = n
    else:
        uris = None

    source_records = ""
    if 'source_records' in j:
        for n in j['source_records']:
            source_records = n
    else:
        source_records = None

    uri_descriptions = ""
    if 'uri_descritions' in j:
         for n in j['uri_descriptions']:
              uri_descriptions = n
    else:
         uri_descriptions = None

    c.execute(
        'INSERT INTO EDITION VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        [record['key'],
         j.get('title'),
         j.get('title_prefix'),
         j.get('subtitle'),
         other_titles,
         j.get('by_statement'),
         j.get('publish_date'),
         j.get('copyright_date'),
         j.get('edition_name'),
         description,
         notes,
         genres,
         work_titles,
         series,
         j.get('physical_dimensions'),
         j.get('physical_format'),
         j.get('number_of_pages'),
         subjects,
         j.get('pagination'),
         lccn,
         j.get('ocaid'),
         oclc_numbers,
         isbn_10,
         isbn_13,
         dewey_decimal_class,
         lc_classifications,
         contributions,
         publish_places,
         j.get('publish_country'),
         publishers,
         distributors,
         j.get('first_sentence'),
         j.get('weight'),
         location,
         j.get('scan_on_demand'),
         uris,
         uri_descriptions,
         j.get('translation_of'),
         source_records,
         j.get('accompanying_material')])

db.commit()