from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/signIn', methods=['GET', 'POST'])
def login():
 return render_template("signInVa.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
 logout_user()
 return redirect(url_for('auth.login'))

@auth.route('/Verify', methods=['GET', 'POST', 'PUT'])
@login_required
def verify():
 return render_template("identityVerificationVa.html", user=current_user)

@auth.route('/SignUp', methods=['GET', 'POST', 'PUT'])
def sign_up():
 return render_template("signUpVa.html", user=current_user)

#@auth.route('/SignUp', methods=['GET', 'POST', 'PUT'])
#def sign_up():
# return render_template("signUpVa.html", user=current_user)
