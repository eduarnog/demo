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