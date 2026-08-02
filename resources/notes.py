from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.dbconfig import db
from models.note import Note


class Notes(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()

        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return {
                "error": "Title and content are required."
            }, 400

        note = Note(
            title=title,
            content=content,
            user_id=int(get_jwt_identity())
        )

        db.session.add(note)
        db.session.commit()

        return note.to_dict(), 201