from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField, BooleanField, TextAreaField, TelField, IntegerField
from wtforms.validators import DataRequired, URL, NumberRange

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