#redirect me sirve para redireccionar  #Flash sirve para crear datos pequeños (mensajes)
from flask import render_template, redirect,flash
from . import productos
import app 
from .forms import NewProductForm,EditProductForm
import os

#rutas de el modulo ""productos""
@productos.route("listar")
def listar():
        # listar los productos utilizando 
    # modelos
    productos = app.models.Producto.query.all()   
    return  render_template("index.html",productos = productos)
    

@productos.route("/nuevo", methods = ["GET", "POST"])
def nuevo():
    #definir el formulario
    form = NewProductForm()
    #definir el objeto producto
    p = app.models.Producto()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename 
        app.db.session.add(p)
        app.db.session.commit()
           
        # return os.getcwd()

        # Extraer el objeto FileStorage
        file = form.imagen.data
        file.save(os.path.abspath(os.getcwd()+"/app/productos/imagenes/" + form.imagen.data.filename))
        
        flash("Producto registrado correctamente :D")

        return redirect("/productos/listar") 
    
    
    return render_template("new.html",operacion="Nuevo",  form=form)


@productos.route("/editar/<producto_id>", methods = ["GET", "POST"])
def editar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    form = EditProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Producto actualizado correctamente :D")
        return redirect("/productos/listar") 

    return render_template("new.html",
                           operacion="Actualizar", 
                           form = form)



@productos.route('/eliminar/<producto_id>')
def eliminar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Producto eliminado")
    return redirect("/productos/listar")