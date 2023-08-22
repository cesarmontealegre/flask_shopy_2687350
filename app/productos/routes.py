from flask import render_template
from . import productos
import app
from .forms import RegistrarProductoForm

#Rutas del Modulo productos
@productos.route("/listar")
def listar():
    #Listar los productos utilizando modelos
    productos = app.models.Producto.query.all()
    return render_template("index.html",
                           productos = productos)

@productos.route("/nuevo", 
                 methods = ["GET", "POST"])
def nuevo():
    #Definir el formulario
    form = RegistrarProductoForm()
    #Definir el objeto producto
    p = app.models.Producto()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return "Producto Registrado"
    return render_template("new.html",
                           form = form)