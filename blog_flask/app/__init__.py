from flask import Flask


from app.models.base import db
from flask_cors import *




def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.article import web
    app.register_blueprint(web)