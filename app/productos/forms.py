from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrarProductoForm(FlaskForm):
    nombre = StringField("Nombre del producto:")
    precio = StringField("Precio del producto:")
    submit = SubmitField("Guardar")