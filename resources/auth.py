from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from models.dbconfig import db
from models.user import User


class Signup(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")
        password_confirmation = data.get("password_confirmation")

        if not username or not password:
            return {
                "error": "Username and password are required."
            }, 400

        if password != password_confirmation:
            return {
                "error": "Passwords do not match."
            }, 400

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return {
                "error": "Username already exists."
            }, 409

        user = User(
            username=username,
            email=f"{username}@example.com"
        )

        user.password = password

        db.session.add(user)
        db.session.commit()

        token = create_access_token(identity=str(user.id))

        return {
            "token": token,
            "user": user.to_dict()
        }, 201


class Login(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {
                "error": "Username and password are required."
            }, 400

        user = User.query.filter_by(username=username).first()

        if not user or not user.authenticate(password):
            return {
                "error": "Invalid username or password."
            }, 401

        token = create_access_token(identity=str(user.id))

        return {
            "token": token,
            "user": user.to_dict()
        }, 200


class Me(Resource):
    @jwt_required()
    def get(self):
        user_id = int(get_jwt_identity())

        user = User.query.get(user_id)

        if not user:
            return {
                "error": "User not found."
            }, 404

        return user.to_dict(), 200