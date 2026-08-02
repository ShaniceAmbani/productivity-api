from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config import Config
from models.dbconfig import db, migrate
from models.user import bcrypt
from resources.auth import Signup, Login

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)

jwt = JWTManager(app)
api = Api(app)

api.add_resource(Signup, "/signup")
api.add_resource(Login, "/login")


@app.route("/")
def home():
    return {
        "message": "Productivity API is running!"
    }


if __name__ == "__main__":
    app.run(debug=True)