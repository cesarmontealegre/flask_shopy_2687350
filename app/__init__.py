from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from .mi_blueprint import mi_blueprint
from app.productos import productos
# crear el objeto de aplicación
app = Flask(__name__)
app.config.from_object(Config)

# crear el objeto sqlalchemy
db = SQLAlchemy(app)

#crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

#Configurar bootstrap con app
bootstrap = Bootstrap(app)

#Se registra el nuevo modulo
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

#Traer los modelos
from .models import Producto, Cliente, Detalle, Venta