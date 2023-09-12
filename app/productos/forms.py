from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField,FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange


class RegistrarProductoForm():
    nombre = StringField("Nombre del producto: " ,validators = [InputRequired(message="Debe de ingresar el nombre de un producto")] )
    precio = IntegerField("Precio del producto: " , validators=[InputRequired(message="Debe de ingresar el precio del producto"),
                                                                NumberRange(message="Precio fuera del rango ", min= 10, max=100000)
                                                                ])
    
class NewProductForm(FlaskForm,RegistrarProductoForm):    
    imagen = FileField("Seleccione Imagen del producto: ", validators= [FileRequired(message="Por favor seleccione una imagen"), FileAllowed(['jpg','png'],"solo se permiten archivos jpg y png" )])
    submit = SubmitField("Guardar")



class EditProductForm(FlaskForm,RegistrarProductoForm):
    submit = SubmitField("Actualizar")