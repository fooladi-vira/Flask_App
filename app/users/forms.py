from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.users.models import User

class UserRegisteratinForm(FlaskForm):
   username=StringField('user name ',validators=[DataRequired(),Length(min=4,max=25,message='user name must be 4-25 character')])
   email = StringField('email', validators=[DataRequired(), Email(message='your email is incorrect')])
   password=PasswordField('password ',validators=[DataRequired()])
   confirm_password=PasswordField(' repeated password ',validators=[DataRequired(),EqualTo('password',message='your password is not same')] )
   submit=SubmitField('register')
   def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('this user name exist...')
   def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('this email exist...')
            
    
class UserLoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),  Email(message='your email is incorrect')])
    password=PasswordField('password ',validators=[DataRequired()])
    remember=BooleanField(label='remember me')
    submit=SubmitField('log in')
    
class UpdateProfileForm(FlaskForm):
    username=StringField('user name',validators=[DataRequired(),Length(min=4,max=25,message='user name must be 4-25 character')])
    email = StringField('email', validators=[DataRequired(), Email(message='your email is incorrect')])
    
    submit=SubmitField('update ')
    def validate_username(self,username):
        if username.data!= current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('this user name exist...')
    def validate_email(self,email):
        if email.data!= current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('this email exist...')
    