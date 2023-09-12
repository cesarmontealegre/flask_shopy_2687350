from flask import Blueprint

# Defino el modulo llamado mi_blueprint
mi_blueprint = Blueprint('blueprint',__name__, url_prefix= '/blueprint')


#creo funcionalidad para el modulo 
@mi_blueprint.route("/ejemplo")

def ejemplo():
    return "este es el ejemplo"