"""import csv
import sys
import json
import sqlite3



COLUMNS    = ['type','key','revision','last_modified','json']
INPUT_FILE = '../data/small-authors.txt'
#INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
#DB_FILE = 'opendata.db'
#DB_FILE = 'databases.db'
DB_FILE = '../bdd/databases.db'
#DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema.sql'


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

"""
"""
import csv
import sys
import json
import sqlite3

import nltk


COLUMNS    = ['type','key','revision','last_modified','json']
INPUT_FILE = '../data/small-authors.txt'
#INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
#DB_FILE = 'opendata.db'
DB_FILE = '../bdd/databases.db'
#DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema.sql'

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript(open(DB_SCHEMA,'r').read())







# # keys = set()
# i = 1
## try:
#     for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
#         #print(record['type'],record['key'],record['revision'])
#         # key = record['key']
#         # if key in keys:
#         #     print("BAM",key,record)
#         #     sys.exit(1)
#         # keys.add(key)
#         i += 1
# except:
#     print(i) cest quoi ton pb 200 IQ

#Je vois pas commment tu veux que je prenne les valeurs de noms, puisque t'as pas de sql tout ça



for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
     j = json.loads(record['json'])     #print(record['key'],j['key'],record['key'] == j['key'],j.get('name'),j.get('birth_date'),j.get('death_date'),j.get('title'),j.get('bio'))
     #c.execute('INSERT INTO AUTHOR VALUES (?,?,?)',[record['key'],j['name'],j.get('birth_date')])
     c.execute('INSERT INTO AUTHORS VALUES (?,?,?,?,?,?,?,?,?,?,?)',[record['key'],j.get('name'),j.get('eastern_order'),j.get('personal_name'),j.get('enumeration'),j.get('title'),j.get('location'),j.get('birth_date'),j.get('death_date'),j.get('date'),j.get('wikipedia')])
     #print(j.get('name'))
db.commit()

valeur=[]
valeur2=[]


req = "select * from AUTHORS"
result = c.execute(req)
print(type(result))
rows = c.fetchall()
for row in rows:
    valeur.append((' {1} '.format(row[0], row[1],)))
    valeur2.append((' {1} '.format(row[0], row[7],)))

x=0
liste=[]
#print(valeur2)

for x in range(len(valeur)):
    for i in range(x+1,len(valeur)):
        ed = nltk.edit_distance(valeur[x],valeur[i])
        dico={"titre":valeur[x],"titre_compare":valeur[i], "distance":ed}
        a=(dico["titre"]),"&&",(dico["titre_compare"]),"&&",(dico["distance"])
        if ((dico["distance"])<7 and dico["titre"]!= ' None ') and dico["titre_compare"] !=' None ':
            print(dico["titre"],"COMPARE TO",dico["titre_compare"],"DISTANCE =",dico["distance"],"&&",x)
            for l in range(len(valeur2)):
                for y in range(l + 1, len(valeur2)):
                    ed2 = nltk.edit_distance(valeur2[l], valeur2[y])
                    dico2 = {"titre2": valeur2[l], "titre_compare2": valeur2[y], "distance2": ed2}
                    a2 = (dico2["titre2"]), "&&", (dico2["titre_compare2"]), "&&", (dico2["distance2"])
                    if ((dico2["distance2"]) < 7 and dico2["titre2"] != ' None ') and dico2["titre_compare2"] != ' None ':
                        print(dico2["titre2"], "COMPARE TO", dico2["titre_compare2"], "DISTANCE =", dico2["distance2"], "&&", l)

#print(liste[0])





#liste2=[]


#for row in rows:
#	liste.append((' {1} '.format(row[0], row[3], )))


#for y in range(len(liste)):
#	for z in range(y + 1, len(liste)):
#		ed = nltk.edit_distance(valeur[y], valeur[z])
#	dico = {"titre": valeur[y], "titre_compare": liste[z], "distance": ed}
#	(dico["titre"]), "&&", (dico["titre_compare"]), "&&", (dico["distance"])

        #if ((dico["distance"]) < 7 and dico["titre"] != ' None ') and dico["titre_compare"] != ' None ':
#	print(dico["titre"], "&&", dico["titre_compare"], "&&", dico["distance"], "&&", y, "&&", z)
#	liste2.append((dico["titre"], "&&", dico["titre_compare"], "&&", dico["distance"], "&&", y, "&&", z))




#print(liste2)

#  -----> Marche pas



















# la jsp mais si tu veux faire des requtes fait les direct dans la base , apres tu regarderas pour comparer les valeurs entre elles ici,  bah justement je c
#ATT, CJuosmcomment je compare les valeurs entre elles si je peux pas faire de requete sql sur pyhon, bah si j'ai pas réflechi encore de base cétait ton job,

for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
    j = json.loads(record['json'])
    # if 'alternate_names' in j:
    #     print("YES",j['name'])
    #     for n in j['alternate_names']:
    #         print("   ",n)

"""

import csv
import sys
import json
import sqlite3

import nltk

COLUMNS = ['type', 'key', 'revision', 'last_modified', 'json']
INPUT_FILE = '../data/small-authors.txt'
# INPUT_FILE = 'data/ol_dump_authors_2020-02-29.txt'
# DB_FILE = 'opendata.db'
DB_FILE = '../bdd/databases.db'
# DB_FILE = ":memory:"
DB_SCHEMA = '../sql/schema.sql'

db = sqlite3.connect(DB_FILE)
c = db.cursor()

c.executescript(open(DB_SCHEMA, 'r').read())

# # keys = set()
# i = 1
## try:
#     for record in csv.DictReader(open(INPUT_FILE,'r'),fieldnames=COLUMNS,delimiter='\t'):
#         #print(record['type'],record['key'],record['revision'])
#         # key = record['key']
#         # if key in keys:
#         #     print("BAM",key,record)
#         #     sys.exit(1)
#         # keys.add(key)
#         i += 1
# except:
#     print(i) cest quoi ton pb 200 IQ

# Je vois pas commment tu veux que je prenne les valeurs de noms, puisque t'as pas de sql tout ça


for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
    j = json.loads(record['json'])

    if 'bio' in j and 'value' in j['bio']:
        bio = j['bio']['value']
    else:
        bio = None

    alternate_names = ""
    if 'alternate_names' in j:
        for n in j['alternate_names']:
            alternate_names = n
    else:
        alternate_names = None

    uris = ""
    if 'uris' in j:
        for n in j['uris']:
            uris = n
    else:
        uris = None

    links_title = ""
    links_url = ""
    if 'links' in j:
        for n in j["links"]:
            links_url = n['url']
            links_title = n["title"]
    else:
        links_url = None
        links_title = None

    c.execute('INSERT INTO AUTHORS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
              [record['key'],
               j.get('name'),
               j.get('eastern_order'),
               j.get('personal_name'),
               j.get('enumeration'),
               j.get('title'),
               bio,
               alternate_names,
               uris,
               j.get('location'),
               j.get('birth_date'),
               j.get('death_date'),
               j.get('date'),
               j.get('wikipedia'),
               links_url,
               links_title])
db.commit()


valeur=[]
listee=[]
req = "select * from AUTHORS"
result = c.execute(req)
print(type(result))
rows = c.fetchall()
for rowz in rows:
    listee.append((' {1} '.format(rowz[0], rowz[3], )))
for row in rows:
    valeur.append((' {1} '.format(row[0], row[1],)))


x=0
liste=[]
for x in range(len(valeur)):
    for i in range(x+1,len(valeur)):
        ed = nltk.edit_distance(valeur[x],valeur[i])
        dico={"titre":valeur[x],"titre_compare":valeur[i], "distance":ed,"x":x,"i":i}
        a=((dico["titre"]),"&&",(dico["titre_compare"]),"&&",(dico["distance"]),"&&",(dico["x"]),"&&",(dico["i"]))

        if ((dico["distance"])<7 and dico["titre"]!= ' None ') and dico["titre_compare"] !=' None ':
            a=print(dico["titre"],"&&",dico["titre_compare"],"&&",dico["distance"],"&&",dico["x"],"&&",dico["i"])
            liste.append((dico["titre"],"&&",dico["titre_compare"],"&&",dico["distance"],"&&",dico["x"],"&&",dico["i"]))
            ed2 = nltk.edit_distance(listee[dico["x"]], listee[dico["i"]])
            print(listee[dico["x"]], listee[dico["i"]],ed2)
"""

for record in csv.DictReader(open(INPUT_FILE, 'r'), fieldnames=COLUMNS, delimiter='\t'):
    j = json.loads(record['json'])
    if 'links' in j:
        for n in j["links"]:
            print("  lalala ", n)
            links_url.append(n['url'])
            links_title.append(n["title"])
            # for k in n:
            # print(k['url'])

print(links_url)
print(links_title)

    if 'links' in j:
        for link in j['links']:
            #dico = ({'url': link['url']})
            #dico2 = ({'title': link['title']})
            for i in link['url']:
                links_url = i
            for j in link['title']:
                links_title = j
    else:
        links_url = None
        links_title = None
"""
