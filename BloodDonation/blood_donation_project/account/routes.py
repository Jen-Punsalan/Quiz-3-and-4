from flask import render_template, request, redirect, url_for
from . import account
from .models import User
from app import db

@account.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['jen']
        email = request.form['jpnsln@hau.edu.ph']
        password = request.form['cpe201']
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('account.login'))
    return render_template('account/register.html')

@account.route('/login', methods=['GET', 'POST'])
def login():
    # Implement login logic here
    return render_template('account/login.html')

@account.route('/profile')
def profile():
    # Implement profile logic here
    return render_template('account/profile.html')
