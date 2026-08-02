from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from models.dbconfig import db
from models.user import User


class Signup(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return {
                "error": "Username, email and password are required."
            }, 400

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            return {
                "error": "Username or email already exists."
            }, 409

        user = User(
            username=username,
            email=email
        )

        user.password = password

        db.session.add(user)
        db.session.commit()

        token = create_access_token(identity=str(user.id))

        return {
            "message": "User created successfully.",
            "access_token": token,
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
            "message": "Login successful.",
            "access_token": token,
            "user": user.to_dict()
        }, 200