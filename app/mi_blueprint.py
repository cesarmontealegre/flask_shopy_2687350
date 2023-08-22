from flask import Blueprint

#Se define el modulo llamado mi_bluprint
mi_blueprint = Blueprint ('blueprint',
                          __name__, 
                          url_prefix = '/blueprint')

#Se crea una funcionalidad para el modulo
@mi_blueprint.route("/ejemplo")
def ejemplo():
    return "Este es el gordis :3"