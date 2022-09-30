import datetime
import re
from flask import Flask, render_template, request
from peewee import MySQLDatabase, Model, CharField, TextField, BooleanField, DateTimeField, IntegerField, OperationalError
from forms import AdaugaForm, ModificaForm

right_now = datetime.datetime.now()

mysql_db = MySQLDatabase('camine', user='root', password='AnaFilipDelia2022!', host='127.0.0.1', port=3306, charset='utf8mb4')

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

app.config['SECRET_KEY'] = 'fa11dd842bf8374664a9e72fb4eecabe26b3416a21910dffa4'

@app.route("/")
@app.route("/index")
def index():
    camine = Camin.select()
    return render_template("index.html", camine=camine)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AdaugaForm()
    if request.method == "POST":
        print("post data:")
        # nume = request.form['nume']
        # adresa = request.form['adresa']
        # site = request.form['site']
        # telefon = request.form['telefon']
        # pret = request.form['pret']
        # verificat = request.form['verificat']
        # note = request.form['note']

        # print(f'Nume: {nume}\nAdresa: {adresa}\nSite: {site}\nTelefon: {telefon}\nPret: {pret}\nNote: {note}\n')
        print(request.form.getlist('verificat'))
    return render_template("add.html", form=form)

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    form = ModificaForm()
    camine = Camin.select()
    camin = Camin.select().where(Camin.id == id).get()
    if request.method == "POST":
        pass
    return render_template("update.html", camin=camin, camine=camine, form=form)

if __name__ == "__main__":
    app.run(debug=True)