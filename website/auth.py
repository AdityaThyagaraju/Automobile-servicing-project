from flask import redirect,url_for,Blueprint, render_template,request,flash
from .models import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required,current_user
auth = Blueprint('auth',__name__)

@auth.route('/Login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usn = request.form.get('Username')
        pwd = request.form.get('Password')
        user = User.query.filter_by(username=usn).first()
        if user:
            if user.role=='C':
                if check_password_hash(user.password,pwd):
                    login_user(user,remember=True)
                    flash('Logged in successfully',category='success')
                    return redirect(url_for('views.customer'))
                else:
                    flash('Password incorrect',category='error')
            elif user.role=='S':
                if check_password_hash(user.password,pwd):
                    login_user(user,remember=True)
                    flash('Logged in successfully',category='success')
                    return redirect(url_for('views.staff'))
                else:
                    flash('Password incorrect',category='error')
        else:
            flash(['Login','User does not exist, please register first'])
    return redirect(url_for('views.home'))

@auth.route('/Logout')
@login_required
def logout():
    logout_user()
    flash('Logged out succesfully',category='success')    
    return redirect(url_for('auth.login'))


@auth.route('/Signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        chk = request.form.get('cbtn')
        name = request.form.get('name')
        usn = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        user = User.query.filter_by(username=usn).first()
        if user :
            flash('Email already exist',category='error')
        elif len(usn)>20 and len(usn)<8:
            flash(['Sign up','Not a valid username, length is not within limits'],category='error')
        elif password!=repassword:
            flash(['Sign up','Password doesnt match with re-entered password'],category='error')
        else :
            if chk == 0:
                new_user = User(name=name,role='C',email=email,password=generate_password_hash(password,method='sha256'),username=usn)
                db.session.add(new_user)
                db.session.commit()
                flash(['Sign up','Account created'],category='success')
                return redirect(url_for('views.home'))
            else :
                new_user = User(name=name,role='S',email=email,password=generate_password_hash(password,method='sha256'),username=usn)
                db.session.add(new_user)
                db.session.commit()
                flash(['Sign up','Account created'],category='success')
                return redirect(url_for('views.home'))
    return render_template('index.html')