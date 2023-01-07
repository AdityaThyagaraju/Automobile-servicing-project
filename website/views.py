from flask import Blueprint, render_template,request,flash,jsonify
from flask_login import current_user,login_required
from .models import Note
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    # if request.method == 'POST':
    #     note = request.form.get('Note')
    #     if len(note)<1:
    #         flash('Cannot add empty note!',category='error')
    #     else:
    #         new_note = Note(data=note,user_id = current_user.id)
    #         db.session.add(new_note)    
    #         db.session.commit()
    #         flash('Note added',category='success')
    return render_template("customer.html")

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteId']
    qr_note = Note.query.get(noteID)
    if qr_note:
        if qr_note.user_id==current_user.id:
            db.session.delete(qr_note)
            db.session.commit()
            flash('deleted note',category='success')
            return jsonify({})