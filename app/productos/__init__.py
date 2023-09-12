from flask import Blueprint
productos = Blueprint('productos',__name__,url_prefix='/productos',template_folder='templates',static_folder = 'imagenes' )

#vincular el archivo de rutas 
from . import routes