from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField, BooleanField, TextAreaField, TelField, IntegerField
from wtforms.validators import DataRequired, URL, NumberRange, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired

class AdaugaForm(FlaskForm):
    nume = StringField('Nume', validators=[DataRequired()])
    adresa = StringField('Adresa')
    site = URLField('Site', validators=[URL()])
    telefon = TelField('Telefon')
    pret = IntegerField('Pret', validators=[NumberRange(min=0, max=10000)])
    verificat = BooleanField('Camin Verificat')
    note = TextAreaField('Observatii')
    salveaza = SubmitField('Salveaza')


class ModificaForm(FlaskForm):
    nume = StringField('Nume', validators=[DataRequired()])
    adresa = StringField('Adresa')
    site = URLField('Site', validators=[URL()])
    telefon = TelField('Telefon')
    pret = IntegerField('Pret', validators=[NumberRange(min=0, max=10000)])
    verificat = BooleanField('Camin Verificat')
    note = TextAreaField('Observatii')
    salveaza = SubmitField('Modifica')

class IncarcaPoze(FlaskForm):
    imagini = FileField('Imagini', validators=[FileRequired('Trebuie sa alegeti un fisier'), FileAllowed(['jpg', 'jpeg', 'png'], 'Este permisa doar incarcarea de imagini')])
    incarca = SubmitField('Incarca')