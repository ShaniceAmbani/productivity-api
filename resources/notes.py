from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.dbconfig import db
from models.note import Note


class Notes(Resource):
    @jwt_required()
    def get(self):
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)

        user_id = int(get_jwt_identity())

        pagination = (
            Note.query.filter_by(user_id=user_id)
            .order_by(Note.created_at.desc())
            .paginate(page=page, per_page=per_page, error_out=False)
        )

        return {
            "notes": [note.to_dict() for note in pagination.items],
            "page": pagination.page,
            "pages": pagination.pages,
            "total": pagination.total
        }, 200

    @jwt_required()
    def post(self):
        data = request.get_json()

        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return {"error": "Title and content are required."}, 400

        note = Note(
            title=title,
            content=content,
            user_id=int(get_jwt_identity())
        )

        db.session.add(note)
        db.session.commit()

        return note.to_dict(), 201


class NoteByID(Resource):
    @jwt_required()
    def patch(self, id):
        note = Note.query.get(id)

        if not note:
            return {"error": "Note not found."}, 404

        if note.user_id != int(get_jwt_identity()):
            return {"error": "Unauthorized."}, 403

        data = request.get_json()

        if "title" in data:
            note.title = data["title"]

        if "content" in data:
            note.content = data["content"]

        db.session.commit()

        return note.to_dict(), 200

    @jwt_required()
    def delete(self, id):
        note = Note.query.get(id)

        if not note:
            return {"error": "Note not found."}, 404

        if note.user_id != int(get_jwt_identity()):
            return {"error": "Unauthorized."}, 403

        db.session.delete(note)
        db.session.commit()

        return {"message": "Note deleted successfully."}, 200