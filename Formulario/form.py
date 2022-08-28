"""Módulos"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Datos(FlaskForm):
    """Datos obtenidos del Formulario"""
    nombre = StringField("Nombre", validators=[
        DataRequired(), Length(min=3, max=50)])
    correo = StringField("Correo", validators=[
        DataRequired(), Email()])
    telefono = StringField("Telefono", validators=[
        DataRequired(), Length(max=8)])
    submit = SubmitField('Enviar')
