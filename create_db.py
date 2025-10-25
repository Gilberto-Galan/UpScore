from app import create_app, db

# Crear la aplicación
app = create_app()

# Establecer el contexto de la aplicación
with app.app_context():
    db.create_all()  # Crear las tablas en la base de datos
    print("Base de datos creada.")
