import datetime
from flask import Flask, render_template
from peewee import MySQLDatabase, Model, CharField, TextField, BooleanField, DateTimeField, IntegerField, OperationalError

right_now = datetime.datetime.now()

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

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    camine = Camin.select()
    return render_template("index.html", camine=camine)

@app.route("/add")
def add():
    camine = Camin.select()
    return render_template("add.html", camine=camine)


if __name__ == "__main__":
    app.run(debug=True)