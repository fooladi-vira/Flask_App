from app.database import BaseModel
from app.extentions import db
from flask_login import UserMixin

class Post(BaseModel,UserMixin):
    
    title=db.Column(db.String(120), nullable=False)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f'< {self.__class__.__name__} <id==>> {self.id}  <title >  {self.title} ' 