import sys
from flask import render_template, flash, redirect, url_for, jsonify
import sqlalchemy as sqla

from app import db
from app.main.models import Post, Tag, User
from flask_login import current_user, login_required
from app.main.forms import PostForm, SortForm

from app.main import main_blueprint as bp_main

@bp_main.route('/', methods=['GET', 'POST'])
@bp_main.route('/index', methods=['GET'])
@login_required
def index():    
    sform = SortForm()
    if sform.validate_on_submit():
        choice = sform.selection.data
        attribute = ''
        if sform.my_posts.data:
            myposts = current_user.get_post_relationship()  
        else:
            myposts = sqla.select(Post)
        if int(choice) == 3:
                posts = db.session.scalars(myposts.order_by(Post.title))
        elif int(choice) == 2:
            posts = db.session.scalars(myposts.order_by(Post.likes.desc()))
        elif int(choice) == 1:
            posts = db.session.scalars(myposts.order_by(Post.happiness_level.desc()))
        else:
            posts = db.session.scalars(myposts.order_by(Post.timestamp.desc()))
        all_posts = posts.all()
    else:
        posts = db.session.scalars(sqla.select(Post).order_by(Post.timestamp.desc()))
        all_posts = posts.all() 
    return render_template('index.html', title="Smile Portal", posts=all_posts, current__user = current_user, form = sform)

@bp_main.route('/post/create', methods=['GET', 'POST'])
@login_required
def postsmile():
    pform = PostForm()
    if pform.validate_on_submit():
        new_post = Post(user_id = current_user.id,
                        title = pform.title.data,
                        happiness_level = pform.happiness_level.data,
                        body = pform.body.data)
        for t in pform.tag.data:
            new_post.tags.add(t)

        db.session.add(new_post)
        db.session.commit()
        flash('Post "' + new_post.title + '" is created!')
        return redirect(url_for('main.index'))

    return render_template('create.html', current__user = current_user, form=pform)

@bp_main.route('/post/<post_id>/like', methods=['GET', 'POST'])
@login_required
def like(post_id):
    post = db.session.get(Post, post_id)
    post.likes = post.likes + 1
    db.session.add(post)
    db.session.commit()
    post = db.session.get(Post, post_id)
    data = {'like_count': post.likes,
               'post_id': post.id}
    return jsonify(data)


@bp_main.route('/posts/<post_id>/tags', methods=['GET'])
@login_required
def get_post_tags(post_id):
    thepost = db.session.get(Post, post_id)
    tags = thepost.get_tags()
    return render_template( '_post.html',
                           title = 'Tags in Post "{}"'.format(thepost.title),
                           post = thepost,
                           tags = tags)

@bp_main.route('/post/<post_id>/delete', methods = ['POST'])
@login_required
def delete_post(post_id):
    thepost = db.session.get(Post, post_id)
    name = thepost.title
    if thepost != None:
        for t in thepost.get_tags():
            thepost.tags.remove(t)
            db.session.commit()
        db.session.delete(thepost)
        db.session.commit()
        flash('Post "' + name + '" is deleted.')
    return redirect(url_for('main.index'))



