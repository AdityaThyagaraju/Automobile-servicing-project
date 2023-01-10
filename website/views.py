from flask import Blueprint, render_template,request,flash,jsonify,redirect,url_for
from flask_login import current_user,login_required
from .models import Feedback,User,Customerveh,ReqSer
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
     return render_template("staff.html")

@views.route('/customer',methods=['GET','POST'])
def customer():
    if request.method == 'POST':
        if Customerveh.query.all()<=100:
            brand = request.form.get('brand')
            model = request.form.get('model')
            ch_no = request.form.get('chasis_no')
            service = request.form.getlist('service')
            seldate = request.form.get('seldate')
            new_veh = Customerveh(brand=brand,model=model,chasis_no=ch_no,selected_date=seldate,cust_id=current_user.id)
            veh = Customerveh.query.filter_by(chasis_no=ch_no).first()
            if veh:
                flash(['Error','Vehicle with this chasis no already exists'])
                return redirect(url_for('views.customer'))
            else:
                db.session.add(new_veh)
                db.session.commit()
                queryveh = Customerveh.query.filter_by(chasis_no=ch_no).first()
                for ser in service:
                    new_ser = ReqSer(veh_id=queryveh,req=ser)
                    db.session.add(new_ser)
                    db.session.commit()
                    flash('Request applied, please wait for confirmation from our side')
        else:
            flash('Pending request for vehicles has overflooded, please try later',category='success')
    check_acc = Customerveh.query.filter_by(cust_id=current_user.id)
    for v in check_acc:
        if v.accepted_by_staff == 1:
            flash(['accept','Vehicle with chasis number: '+str(v.chasis_no)+'is accepted please wait for bill generation'])
    return render_template('customer.html',user = current_user)

@views.route('/customerfeedback',methods=['POST'])
def cust_feedback():
        feedback = request.form.get('feedback')
        new_feedback = Feedback(data=feedback,user_id=current_user.id)
        db.session.add(new_feedback)
        db.session.commit()
        return redirect(url_for('views.customer'))

                                            #   staff-route
# @views.route('/Staff')
# def staff():
#     if request.method == 'POST':



    