import json
from flask import Blueprint, request, jsonify
from flask_login import current_user
from app.notes.models import Note
from app.extensions.database import db

blueprint = Blueprint('notes', __name__)

@blueprint.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@blueprint.route('/edit-note', methods=['POST'])
def edit_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note_data = note['noteData']
    edited_note = Note.query.filter_by(id=note_id, user_id=current_user.id).first()
    if not edited_note:
        flash('You do not have permission to edit this note', category='error')
    else:
        return jsonify({'noteData': edited_note.data})