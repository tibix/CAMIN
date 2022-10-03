import datetime

from peewee import MySQLDatabase, Model, CharField, TextField, BooleanField, DateTimeField, IntegerField, OperationalError, ForeignKeyField
from config import Secrets

right_now = datetime.datetime.now()

secrets = Secrets()

mysql_db = MySQLDatabase(secrets.db, host=secrets.host, port=secrets.port, user=secrets.user, password=secrets.password, charset=secrets.charset)

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

class Poze(BaseModel):
    path = TextField();
    adaugat = DateTimeField(default=right_now)
    camin = ForeignKeyField(Camin, backref='poze')
