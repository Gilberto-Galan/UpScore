# routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db, login_manager  # Asegúrate de importar db y login_manager de app
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('routes', __name__)

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Ruta de Login
@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('routes.home'))
        else:
            flash('Login fallido. Verifica tu usuario o contraseña.', 'danger')

    return render_template('login.html')

# Ruta de Registro
@bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validaciones
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'danger')
            return redirect(url_for('routes.register'))

        if User.query.filter_by(username=username).first():
            flash('El nombre de usuario ya está en uso.', 'danger')
            return redirect(url_for('routes.register'))

        if User.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado.', 'danger')
            return redirect(url_for('routes.register'))

        # Crear el nuevo usuario
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Cuenta creada con éxito. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('routes.login'))

    return render_template('register.html')

# Ruta de inicio
@bp.route("/home")
@login_required
def home():
    return render_template('home.html')

# Ruta de Logout
@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))
