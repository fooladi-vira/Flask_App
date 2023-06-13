
from flask import Blueprint,render_template,redirect,flash,session,url_for,request
from app.users.models import User
from app.users.forms import UpdateProfileForm,UserRegisteratinForm,UserLoginForm
from app.extentions import db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required


blueprint=Blueprint('users',__name__)


@blueprint.route('/')
def home():
    return render_template('users/home.html')

@blueprint.route('/register',methods=['post','get'])
def register():
    form=UserRegisteratinForm()
    if form.validate_on_submit():
        hash_pass=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hash_pass)
        db.session.add(user)
        db.session.commit()
        flash('you are register', "info")
        return redirect(url_for('users.login_page'))
    return render_template('users/register.html',form=form)


@blueprint.route('/login_page',methods=['post','get'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))
    form=UserLoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash('you login successfull','success')
            next_page=request.args.get('next')
            return redirect(next_page if next_page else url_for('users.home'))
        else:
            flash('your password incorrect','danger')
    return render_template('users/login_page.html',form=form)



    
@blueprint.route('/logout',methods=['post','get'])
@login_required
def logout():
    logout_user()
    flash('you logged out','success')
    return redirect(url_for('users.login_page'))



@blueprint.route('/profile',methods=['post','get'])
@login_required
def profile():
    form=UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('your information updated','success')
        return redirect( url_for('users.profile'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data= current_user.email
    return render_template('users/profile.html',form=form)