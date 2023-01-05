from flask import redirect,url_for,Blueprint, render_template,request,flash
from .models import User,Note
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required,current_user
auth = Blueprint('auth',__name__)

@auth.route('/Login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usn = request.form.get('Username')
        pwd = request.form.get('Password')
        user = User.query.filter_by(name=usn).first()
        if user:
            if check_password_hash(user.password,pwd):
                login_user(user,remember=True)
                flash('Logged in successfully',category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Password incorrect',category='error')
        else:
            flash('User does not exist, please register first')
            return redirect(url_for('auth.signup'))
    return render_template('login.html')

@auth.route('/Logout')
@login_required
def logout():
    logout_user()
    flash('Logged out succesfully',category='success')    
    return redirect(url_for('auth.login'))


@auth.route('/Signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        usn = request.form.get('Username')
        email = request.form.get('Email')
        password = request.form.get('Password')
        repassword = request.form.get('RePassword')

        user = User.query.filter_by(name=usn).first()
        if user:
            flash('Email already exist',category='error')
        elif len(usn)>20 and len(usn)<8:
            flash('Not a valid username, length is not within limits',category='error')
        elif password!=repassword:
            flash('Password doesnt match with re-entered password',category='error')
        else :
            new_user = User(email=email,password=generate_password_hash(password,method='sha256'),name=usn)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created',category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html')