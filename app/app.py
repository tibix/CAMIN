import datetime
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect
from shutil import rmtree

from config import Secrets
from forms import AdaugaForm, ModificaForm, IncarcaPoze
from models import Camin, Poze


app = Flask(__name__)
csrf = CSRFProtect(app)
secrets = Secrets()
right_now = datetime.datetime.now()

app.config['SECRET_KEY'] = secrets.app_secret
app.config['UPLOADED_PATH'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/images')
app.config['MAX_CONTENT_LENGTH'] = 10000 * 1024 * 1024

@app.route("/")
@app.route("/index")
def index():
    camine = Camin.select()
    return render_template("index.html", camine=camine)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AdaugaForm()
    if form.validate_on_submit():
        camin = Camin.create(nume=form.nume.data, 
                             adresa=form.adresa.data,
                             site=form.site.data,
                             telefon=form.telefon.data,
                             pret=form.pret.data,
                             note=form.note.data,
                             verificat=int(form.verificat.data),
                             adaugat=datetime.datetime.now())
        camin.save()
        print(camin.id)
        flash(f'Camin "{form.nume.data}" adaugat cu success', 'success')
        return redirect(url_for('index'))
    return render_template("add.html", form=form)


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    form = ModificaForm()
    camin = Camin.select().where(Camin.id == id).get()
    if form.validate_on_submit():
        camin.nume=form.nume.data 
        camin.adresa=form.adresa.data
        camin.site=form.site.data
        camin.telefon=form.telefon.data
        camin.pret=form.pret.data
        camin.note=form.note.data
        camin.verificat=int(form.verificat.data)
        camin.adaugat=datetime.datetime.now()
        camin.save()
        flash(f'Camin "{form.nume.data}" modificat cu success', 'success')
        return redirect(url_for('index'))
    return render_template('update.html', camin=camin, form=form)


@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id):
    camin = Camin.select().where(Camin.id == id).get()
    form = IncarcaPoze()
    if request.method == "POST":
        if form.validate_on_submit():
            i = form.imagini.data
            imagine = secure_filename(i.filename)
            if not os.path.exists(os.path.join(app.config['UPLOADED_PATH'], str(camin.id))):
                save_path = os.makedirs(os.path.join(app.config['UPLOADED_PATH'], str(camin.id)))
                i.save(os.path.join(save_path, imagine))
            else:
                save_path = os.path.join(app.config['UPLOADED_PATH'], str(camin.id))
                i.save(os.path.join(save_path, imagine))
            Poze.create(path="/static/images/"+str(camin.id)+"/"+imagine, adaugat=right_now, camin_id = camin.id  )
            flash(f'Imaginea {imagine} incarcate cu success', 'success')
        else:
            flash(f'A aparut eroare la incarcarea pozelor!', 'danger')
    return render_template("view.html", camin=camin, form=form)


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    camin = Camin.select().where(Camin.id == id).get()
    nume = camin.nume
    try:
        for poza in camin.poze:
            to_delete = Poze.delete().where(Poze.id == poza)
            to_delete.execute()
        flash(f'Pozele pentru camin {nume} au fost sterse din baza de date!', 'success')
    except:
        flash(f'Pozele pentru caminul {nume} nu au putut fii sterse din baza de date!', 'warning')
    
    try:
        camin.delete_instance()
        flash(f'Caminul {nume} a fost sters cu success', 'success')
    except:
        flash(f'Caminul {nume} nu a putut fi sters din baza de date!', 'warning')

    try:
        rmtree(os.path.join(app.config['UPLOADED_PATH'], str(camin.id)))
        flash(f'Poze pentru caminul {nume} au fost sterse de pe disk!', 'success')
    except:
        flash(f'Poze pentru caminul {nume} nu au putut fi sterse de pe disk!', 'warning')

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
