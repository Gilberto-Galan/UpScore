# __init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicializamos las extensiones
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'app', 'templates'))  # Ruta explícita
    
    # Configuraciones de la app
    app.config['SECRET_KEY'] = 'mi_secreto'
    
    # Cambia la ruta a la base de datos para que esté en la carpeta 'db'
    db_path = os.path.join(os.getcwd(), 'db', 'site.db')  # Crea la ruta completa
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'  # Usa la carpeta db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa las extensiones
    db.init_app(app)
    login_manager.init_app(app)

    # Importar las rutas dentro de la función para evitar importación circular
    from app.routes import bp  # Asegúrate de importar el Blueprint
    app.register_blueprint(bp)  # Registrar el Blueprint en la aplicación

    return app
