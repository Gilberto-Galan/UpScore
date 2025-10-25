from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.models import User
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('routes', __name__)

@LoginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

@bp.route("/home")
@login_required
def home():
    return render_template('home.html')

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))
