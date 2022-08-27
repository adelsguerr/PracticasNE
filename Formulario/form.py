
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class Datos(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(), Length(min=3, max=50)])
    correo = StringField("Correo", validators=[
        DataRequired(), Email()])
    telefono = StringField("Telefono", validators=[
        DataRequired(), Lenght(max=8)])
    submit = SubmitField('Enviar')
