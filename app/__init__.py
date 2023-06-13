from flask import Flask

#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

from app.posts.routes import blueprint as posts_blueprint
from app.users.routes import blueprint as users_blueprint
import app.exceptions as app_exception
from app.extentions import db,migrate,login_manager,bcrypt

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


#db=SQLAlchemy(app)
db.init_app(app)

from app.users.models import User # is here due to circular imports for db
migrate.init_app(app,db)
login_manager.init_app(app)
bcrypt.init_app(app)
#flask db init ////  flask db migrate  //// flask db upgrade
# with app.app_context():
#     db.create_all()