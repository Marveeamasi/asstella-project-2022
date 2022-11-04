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
 if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        email = request.form.get('email')
        country = request.form.get('country')
        state = request.form.get('')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        data = f'\nEmail: {email}\nFirstname: {name} \nPassword: {password2}\nage: {age}\ngender: {gender}\n country: {country}\n state: {state}\n'
        print (f'{data}\n')

        user = User.query.filter_by(email=email).first()
#        user = User.query.filter_by(name=name).second()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 8:
            flash('Email must be greater than 7 characters.', category='error')
        elif len(name) < 4:
            flash('First name must be greater than 3 character.', category='error')
        elif len(country) < 5:
         flash('country must be greater than 4 character.', category='error')
        elif len(gender) < 4:
         flash('gender must be greater than 3 character.', category='error')
        elif len(age) == 2:
         flash('age must be equwl to 2 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
#       else:
#            new_user = User(email=email, name=name, age=age, country=country, state=state, gender=gender, password=generate_password_hash(
#                password1, method='sha256'))
#            db.session.add(new_user)
#            db.session.commit()
#            login_user(new_user, remember=True)
#            flash('Account created!', category='success')
#            return redirect(url_for('views.Genhome')) 
 return render_template("signUpVa.html", user=current_user)
