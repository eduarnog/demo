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
        note_id = request.form.get('note_id')
        note_data = request.form.get('note')

        if note_id: # Editing an existing note
            note = Note.query.get(note_id)
            if note.user_id != current_user.id:
                flash('You do not have permission to edit this note', category='error')
            elif len(note_data) < 1:
                flash('Note is too short!', category='error') 
            else:
                note.data = note_data
                note.edited = True
                db.session.commit()
                flash('Note edited!', category='success')
        else: # Adding a new note
            if len(note_data) < 1:
                flash('Note is too short!', category='error') 
            else:
                new_note = Note(data=note_data, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')

    notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date.desc()).all()
    return render_template('simple_pages/dashboard.html', notes=notes)