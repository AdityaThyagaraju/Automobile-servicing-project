from flask import Blueprint, render_template,request,flash,jsonify,redirect,url_for
from flask_login import current_user,login_required
from .models import Note,User,Customerveh,ReqSer
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    #  if request.method == 'POST':
    #     note = request.form.get('Note')
    #     if len(note)<1:
    #         flash('Cannot add empty note!',category='error')
    #     else:
    #         new_note = Note(data=note,user_id = current_user.id)
    #         db.session.add(new_note)    
    #         db.session.commit()
    #         flash('Note added',category='success')
     return render_template("index.html")

@views.route('/customer',methods=['GET','POST'])
def customer():
    if request.method == 'POST':
        if Customerveh.query.all()<=100:
            brand = request.form.get('brand')
            model = request.form.get('model')
            chasis_no = request.form.get('ch_no')
            req_service = request.form.getlist('req_service')
            selected_slot = request.form.get('sel_slot')
            cust_id = current_user.id
            new_veh = Customerveh(brand=brand,model=model,ch_mo=chasis_no,sel_slot=selected_slot,cust_id=cust_id)
            db.session.add(new_veh)
            for ser in req_service:
                new_ser = ReqSer(veh_id = new_veh.id,request = ser)
                db.session.add(new_ser)
            flash('Request applied, please wait for confirmation from our side')
        else:
            flash('Pending request for vehicles has overflooded, please try later',category='success')
    return render_template('customer.html',user = current_user)

# @views.route('/cust-feedback',methods=['POST'])
# def feedback():
    