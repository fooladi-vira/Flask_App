from flask import Blueprint
from flask  import render_template,redirect,url_for,flash,request,abort
from app.posts.forms import PostForm
from app.posts.models import Post
from app.extentions import db
from flask_login import login_required,current_user
blueprint=Blueprint('posts',__name__)


@blueprint.route('/posts')
def home():
    posts=Post.query.all()
    return render_template('posts/home.html',posts=posts)

@blueprint.route('/post/<int:post_id>')
def detail(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('posts/detail.html',post=post)


@blueprint.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form=PostForm()
    
    if form.validate_on_submit():
       
        post=Post(title=form.title.data,content=form.content.data,auther=current_user)
        db.session.add(post)
        db.session.commit()
        flash('created your project', "info")
        return redirect(url_for('posts.home'))
    
    return render_template('posts/create_project.html',form=form)
    
@blueprint.route('/post/<int:post_id>/delete')
@login_required
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.auther != current_user:
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    flash(' your project deleted  ', "info")
    return redirect(url_for('posts.home')) 

@blueprint.route('/post/<int:post_id>/update',methods=['GET','POST'])
@login_required
def update(post_id):
    post=Post.query.get_or_404(post_id)
    if post.auther != current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
       
        post.title=form.title.data
        post.content=form.content.data 
        db.session.commit()
        flash(' your project updted', "info")
        return redirect(url_for('posts.detail',post_id=post.id))
    elif request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content
    return render_template('posts/update.html',form=form)