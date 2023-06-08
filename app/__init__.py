from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from app.posts.routes import blueprint as posts_blueprint
from app.users.routes import blueprint as users_blueprint
import app.exceptions as app_exception

def register_blueprint(app):
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)

def register_error_handlers(app):
    app.register_error_handler(404,app_exception.page_not_found)
    app.register_error_handler(500,app_exception.server_error)
    

app=Flask(__name__)
register_blueprint(app)
register_error_handlers(app)
app.config.from_object('config.DevConfig')


db=SQLAlchemy(app)

with app.app_context():
    db.create_all()