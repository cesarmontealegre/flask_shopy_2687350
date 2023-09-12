from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField,FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange,Email
from password_validator import PasswordValidator




class RegistrarClienteForm():
    username = StringField("Nombre del cliente: " ,validators = [InputRequired(message="Debe de ingresar el nombre del cliente")] )
    password = IntegerField("Ingrese una contraseña: " , validators=[InputRequired(message="Ingrese una contaseña "),
                                                               NumberRange(message="Debe ingresar una contraseña de minimo 10 ", min=10)])
    email = StringField("Digite el correo del cliente: ", validators=[InputRequired(message="Email del cliente requerido"),Email("ingrese un email correcto")])   

    

   
    

    
class NewClientForm(FlaskForm,RegistrarClienteForm):    
    submit = SubmitField("Guardar")



class EditClientForm(FlaskForm,RegistrarClienteForm):
    submit = SubmitField("Actualizar")