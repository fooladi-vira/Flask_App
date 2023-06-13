from app.database import BaseModel
from app.extentions import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User (BaseModel,UserMixin):
    
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post',backref='auther',lazy=True)
    def __repr__(self):
        return f' {self.__class__.__name__} {self.username}  <email >  {self.email} ' 


