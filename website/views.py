from flask import Blueprint, render_template,request,flash,jsonify,redirect,url_for
import datetime
from sqlalchemy.orm.attributes import flag_modified
from flask_login import current_user,login_required
from .models import Feedback,User,Customerveh,ReqSer,Items,Staffbill,Staffauth
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    
     return render_template("index.html")

@views.route('/customer',methods=['GET','POST'])
def customer():
    if request.method == 'POST':
        if len(ReqSer.query.all())<=100:
            brand = request.form.get('brand')
            model = request.form.get('model')
            ch_no = request.form.get('chasis_no')
            service = request.form.getlist('service')
            seldate = request.form.get('seldate')
            new_veh = Customerveh(brand=brand,model=model,chasis_no=ch_no,cust_id=current_user.id)
            user = User.query.get(int(current_user.id))
            vehicles = user.vehicles
            if vehicles:
                for vehicle in vehicles:
                    if int(ch_no) == vehicle.chasis_no:
                        queryveh = Customerveh.query.filter_by(chasis_no=ch_no).first()
                        veh_ser = ''
                        for ser in service:
                            veh_ser=veh_ser+','+ser
                        new_ser = ReqSer(cust_id=current_user.id,veh_id=queryveh.id,req=veh_ser,selected_date=datetime.datetime.strptime(seldate,'%Y-%m-%d'))
                        db.session.add(new_ser)
                        db.session.commit()
                        flash(['Request','Request applied, please wait for confirmation from our side'])
                        return redirect(url_for('views.customer'))
                
            db.session.add(new_veh)
            db.session.commit()
            queryveh = Customerveh.query.filter_by(chasis_no=ch_no).first()
            veh_ser = ''
            for ser in service:
                veh_ser = veh_ser+' '+ser
            new_ser = ReqSer(cust_id=current_user.id,veh_id=queryveh.id,req=veh_ser,selected_date=datetime.datetime.strptime(seldate,'%Y-%m-%d'))
            db.session.add(new_ser)
            db.session.commit()
            flash(['Request','Request applied, please wait for confirmation from our side'])
        else:
            flash(['Request','Pending request for vehicles has overflooded, please try later'],category='success')
    check_acc = Customerveh.query.filter_by(cust_id=current_user.id).first()
    if check_acc:
        if check_acc.requests:
            for v in check_acc.requests:
                if v.accept_by_staff == 1 and v.flashed == 1:
                    ReqSer.query.filter_by(int(v.id)).update(dict(flashed=1))
                    db.session.commit()
                    flash(['accept','Vehicle with chasis number: '+str(check_acc.chasis_no)+'is accepted please wait for bill generation'])
    return render_template('customer.html',user = current_user)

@views.route('/customer-payment',methods=['POST'])
def cust_payment():
        bill_id = request.form.get('billId')
        feedback = request.form.get('feedback')
        new_feedback = Feedback(data=feedback,user_id=current_user.id)
        db.session.add(new_feedback)
        db.session.commit()
        bill = Staffbill.query.get(int(bill_id))
        bill = Staffbill.query.get(int(bill_id))
        bill.payed = 1
        flag_modified(bill,"payed")
        db.session.merge(bill)
        db.session.commit()
        return redirect(url_for('views.customer'))


                                            #   staff-route
@views.route('/Staff',methods=['POST','GET'])
def staff():
    if request.method == 'POST':
        dec = request.form.get('acc-rej')
        req_id = dec[1:]
        req = ReqSer.query.get(int(req_id))
        if dec[0] == '1':
            
            ReqSer.query.filter_by(id = int(req_id)).update(dict(accept_by_staff=1))
            db.session.commit()
            flash(['Accepted','request with id : '+req_id+' is accepted'])
        elif dec[0] == '0':
            db.session.delete(req)
            db.session.commit()
            flash(['Rejected','request with id : '+req_id+' is rejected'])
    reqlist = []
    requests = ReqSer.query.all()
    for cust_request in requests:
        if cust_request.accept_by_staff == 0:
            reqlist.append(cust_request)
    penlist = []
    pending_payement = Staffbill.query.all()
    for bill in pending_payement:
        if bill.payed == 0:
            penlist.append(bill)
    return render_template('staff.html',reqlist=reqlist,user=current_user,penlist=penlist)



@views.route('/Staff-bill',methods=['POST'])
def staff_bill():
    if request.method == 'POST':
        cust_id = request.form.get('custId')
        chasis_no = request.form.get('chasisNo')
        order_id = request.form.get('orderId')
        service = request.form.getlist('service')
        price = []
        for i in range(1,9):
            p = request.form.get('price'+str(i))
            if len(p)!=0:
                price.append(p)
        vehicles = Customerveh.query.filter_by(cust_id=cust_id)
        for vehicle in vehicles:
            if int(chasis_no) == vehicle.chasis_no:
                sum = 0
                veh = Customerveh.query.filter_by(chasis_no=int(chasis_no)).first()
                for p in price:
                    sum += int(p)
                bill = Staffbill(cust_id=cust_id,veh_id=veh.id,order_id=order_id,amount=sum)
                db.session.add(bill)
                db.session.commit()
                for i in range(len(price)):
                    querbill = Staffbill.query.filter_by(order_id=int(order_id)).first()
                    new_item = Items(name=service[i],price=price[i],bill_id=querbill.id)
                    db.session.add(new_item)
                    db.session.commit()
                flash(['Bill','Successfully generated bill'])
                return redirect(url_for('views.staff'))
    flash(['Error','The customer or vehicle does not exist'])
    return redirect(url_for('views.staff'))
        
@views.route('/Admin',methods=['POST','GET'])
def admin():
    if request.method == 'POST':
        dec = request.form.get('acc-rej')
        stid = dec[1:]
        staff = Staffauth.query.get(int(stid))
        if dec[0] == '1':
            new_user = User(name=staff.name,phone=staff.phone,email=staff.email,username=staff.username,password=staff.password,role='S')
            db.session.add(new_user)
            flash(['Admin','Staff with id :'+stid+' has been authorized'])
        elif dec[0] == '0':
            flash(['Admin','Staff with id :'+stid+' has been rejected'])
        db.session.delete(staff)
        db.session.commit()
    stlist = Staffauth.query.all()
    uslist=User.query.all()
    return render_template('admin.html',stlist=list(stlist),uslist=list(uslist))

@views.route('/Admin-delete',methods=['POST'])
def delete():
    id = request.form.get('acc-id')
    user = User.query.get(int(id))
    db.session.delete(user)
    db.session.commit()
    flash(['Delete','Account with id:'+id+"has been permanently deleted"])
    return redirect(url_for('views.admin'))


    