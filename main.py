import sys
import subprocess
import datetime
import json
from peewee import MySQLDatabase, Model, CharField, TextField, BooleanField, DateTimeField, IntegerField, OperationalError


right_now = datetime.datetime.now()


try:
    import pymysql
except:
    print("There is no Mysql Module Installed")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymysql'])
    import pymysql

mysql_db = MySQLDatabase('camine', user='root', password='', host='127.0.0.1', port=3306, charset='utf8mb4')

class BaseModel(Model):
    class Meta:
        database = mysql_db


class Camin(BaseModel):
    nume = CharField(null=False, index=True, unique=True, max_length=255)
    adresa = TextField(null=True, index=True)
    site = TextField(null=True, index=True)
    telefon = TextField(null=False, index=True)
    pret = IntegerField(null=False, index=True)
    note = TextField(null=True, index=True)
    verificat = BooleanField(null=False, default=False, index=True)
    adaugat = DateTimeField()


def convertJSONtolist(json_file):
    camine = []
    with open(json_file, 'r') as file:
        data = json.load(file)
        for d in data:
            # create dict and add it to camine list
            camin = {
                "nume": d,
                "adresa": data[d]['Adresa'],
                "site": data[d]['Site'],
                "telefon": data[d]['Telefon'],
                "pret": 0,
                "note": "",
                "verificat": False,
                "adaugat": right_now
            }
            camine.append(camin)
    return camine


if __name__ == "__main__":
    try:
        Camin.create_table()
        camine = convertJSONtolist('camine.json')
        Camin.insert_many(camine).execute()
        print("Table populated")
        camine = Camin.select()
        for camin in camine:
            print(camin.site)
    except OperationalError:
        print("Table already exists")
