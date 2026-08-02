from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config import Config
from models.dbconfig import db, migrate
from models.user import bcrypt
from resources.auth import Signup, Login, Me
from resources.notes import Notes, NoteByID

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)

jwt = JWTManager(app)
api = Api(app)

api.add_resource(Signup, "/signup")
api.add_resource(Login, "/login")
api.add_resource(Me, "/me")

api.add_resource(Notes, "/notes")
api.add_resource(NoteByID, "/notes/<int:id>")


@app.route("/")
def home():
    return {"message": "Productivity API is running!"}


if __name__ == "__main__":
    app.run(debug=True)