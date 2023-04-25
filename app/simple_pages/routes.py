from flask import Blueprint, render_template, redirect, url_for, send_file, request, flash
from flask_login import login_user, login_required, current_user
from app.notes.models import Note
from app.users.models import User
from app.extensions.database import db

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
  return render_template('simple_pages/index.html')

@blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template('simple_pages/dashboard.html')