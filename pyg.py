#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# -*- coding: utf-8 -*-
from Database import Database
import csv
import string
db = Database('root','','localhost','phoenix')
query= "select * from `corona_twit`"

def bersih(objek):
    printable = set(string.printable)
    objek = ''.join(filter(lambda x: x in printable, objek))
    return objek
def upload(file_path):
    client_id = "997280757666-6m35pcr9hstp2r9dkcada7tqilii6nn0.apps.googleusercontent.com"
    client_secret = "Obdstp65qrzIDbrJnIQK0TOL"

    try:
        f = open(file_path)
        # Do something with the file

    except IOError:
        print("File not accessible")
    finally:
        f.close()







try:
    db.cursor.execute(query)
    #write into file
    for row in db.cursor:
        x = "aman"
        try:
            with open('dari_db.csv', 'a') as f:
                x = row['Hashtag']
                writer = csv.writer(f)
                if row['Description']:
                    row['Description'] = bersih(row['Description'])
                if row['Text']:
                    row['Text'] = bersih(row['Text'])
                if row['location']:
                    row['location'] = bersih(row['location'])
                if row['Hashtag']:
                    row['Hashtag'] = bersih(row['Hashtag'])

                writer.writerow([row['Time'],row['Description'],row['Usertweets'],row['Source'],row['Target'],
                    row['Verified'],row['Text'],row['Hashtag'],row['location'],row['Following'],row['Followers'],row['Retweets']])

        except Exception as e:
            print('error :',x)


except Exception as e:
    print('ase',e)