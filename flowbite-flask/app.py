import datetime
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect

from config import Secrets
from forms import AdaugaForm, ModificaForm
from models import Camin, Poze


app = Flask(__name__)
dropzone = Dropzone(app)
csrf = CSRFProtect(app)
secrets = Secrets()
right_now = datetime.datetime.now()


app.config['SECRET_KEY'] = secrets.app_secret
app.config['UPLOADED_PATH'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/images')
app.config['DROPZONE_ENABLE_CSRF'] = True
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_MAX_FILE_SIZE'] = 10
app.config['DROPZONE_MAX_FILES'] = 30
app.config['DROPZONE_PARALLEL_UPLOADS'] = 5
app.config['DROPZONE_INVALID_FILE_TYPE'] = 'Doar fisierele tip poze sunt permise.'
app.config['DROPZONE_FILE_TOO_BIG'] = 'Marimea fisierului este mai mare de 10MB. Incercati cu fisiere mai mici!'
app.config['DROPZONE_DEFAULT_MESSAGE'] = '<i class="fa-solid fa-cloud-arrow-up fa-3x"></i><br>Trageti aici pozele pe care doriti sa le incarcati, sau faceti click oriunde in aceasta zona pentru a incarca pozele direct de pe dispozitivul Dvs.!'

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
    return render_template("view.html", camin=camin)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # camin = Camin.select().where(Camin.id == id).get()
    if request.method == 'POST':
        for key,f in request.files.items():
            # if(key.startswith('file')):
            #     if os.path.exists(app.config['UPLOADED_PATH']+ "/" + camin.id):
            #         print("Path exists!")
                filename = secure_filename(f.filename)
                print(filename)
                # f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return redirect(url_for('index'))


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    camin = Camin.select().where(Camin.id == id).get()
    nume = camin.nume
    camin.delete_instance()
    flash(f'Caminul {nume} a fost sters cu success', 'success')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
