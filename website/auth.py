from flask import redirect,url_for,Blueprint, render_template,request,flash
from .models import Customer,Note,Staff
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required,current_user
auth = Blueprint('auth',__name__)

@auth.route('/Login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usn = request.form.get('Username')
        pwd = request.form.get('Password')
        cust = Customer.query.filter_by(username=usn).first()
        staff = Staff.query.filter_by(username=usn).first()
        if cust:
            if check_password_hash(cust.password,pwd):
                login_user(cust,remember=True)
                flash('Logged in successfully',category='success')
                return redirect(url_for('views.customer'))
            else:
                flash('Password incorrect',category='error')
        elif staff:
            if check_password_hash(staff.password,pwd):
                login_user(staff,remember=True)
                flash('Logged in successfully',category='success')
                return redirect(url_for('views.staff'))
            else:
                flash('Password incorrect',category='error')
        else:
            flash('User does not exist, please register first')
    return render_template('views.home')

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
        cust = Customer.query.filter_by(username=usn).first()
        staff = Staff.query.filter_by(username = usn).first()
        if cust or staff :
            flash('Email already exist',category='error')
        elif len(usn)>20 and len(usn)<8:
            flash('Not a valid username, length is not within limits',category='error')
        elif password!=repassword:
            flash('Password doesnt match with re-entered password',category='error')
        else :
            if chk == 0:
                new_user = Customer(name=name,email=email,password=generate_password_hash(password,method='sha256'),username=usn)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created',category='success')
                return redirect(url_for('views.home'))
            else :
                new_user = Staff(name=name,email=email,password=generate_password_hash(password,method='sha256'),username=usn)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created',category='success')
                return redirect(url_for('views.home'))
    return render_template('signup.html')