from flask import redirect,url_for,Blueprint, render_template,request,flash
from .models import User,Staffauth
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_required,current_user
auth = Blueprint('auth',__name__)
#sha256$y78eN6BfaZ7NVLtH$49fd93238657f746d7fa4ae96b1c9dbd399202b7c3262e947a99d18f3e94d14f
@auth.route('/Login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usn = request.form.get('username')
        pwd = request.form.get('password')
        user = User.query.filter_by(username=usn).first()
        if user:
            if user.role=='C':
                if check_password_hash(user.password,pwd):
                    login_user(user,remember=True)
                    flash(['Login','Logged in successfully'],category='success')
                    return redirect(url_for('views.customer'))
                else:
                    flash(['Login','Password incorrect'],category='error')
            elif user.role=='S':
                if check_password_hash(user.password,pwd):
                    login_user(user,remember=True)
                    flash(['Login','Logged in successfully'],category='success')
                    return redirect(url_for('views.staff'))
                else:
                    flash(['Login','Password incorrect'],category='error')
            else :
                if check_password_hash(user.password,pwd):
                    login_user(user,remember=True)
                    flash(['Login','Logged in successfully'])
                    return redirect(url_for('views.admin'))
        else:
            flash(['Login','User does not exist, please register first'])
    return redirect(url_for('views.home'))

@auth.route('/Logout')
@login_required
def logout():
    logout_user()
    flash(['Login','Logged out succesfully'],category='success')    
    return redirect(url_for('auth.login'))


@auth.route('/Signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        chk = request.form.get('cbtn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        usn = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        user = User.query.filter_by(username=usn).first()
        if user :
            flash(['Sign up','Username already exist'],category='error')
        elif len(usn)>20 and len(usn)<8:
            flash(['Sign up','Not a valid username, length is not within limits'],category='error')
        elif password!=repassword:
            flash(['Sign up','Password doesnt match with re-entered password'],category='error')
        else :
            if chk == '0':
                new_user = User(name=name,phone=phone,role='C',email=email,password=generate_password_hash(password,method='sha256'),username=usn)
                db.session.add(new_user)
                db.session.commit()
                flash(['Sign up','Account created'],category='success')
                return redirect(url_for('views.home'))
            elif chk == '1' :
                staff = Staffauth.query.filter_by(username=usn).first()
                if staff :
                    flash(['Sign up','Username already applied'],category='error')
                else:
                    new_user = Staffauth(name=name,phone=phone,email=email,password=generate_password_hash(password,method='sha256'),username=usn)
                    db.session.add(new_user)
                    db.session.commit()
                    flash(['Sign up','Account creation initiated, wait for authorization from admin'],category='success')
                return redirect(url_for('views.home'))
    return render_template('index.html')

    