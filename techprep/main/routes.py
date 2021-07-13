from flask_login import login_required, current_user
from techprep.main.forms import PostForm, CommentForm
from techprep.models import Post, Comment
from techprep import db
from flask import Blueprint, request, render_template, redirect, url_for, flash

main = Blueprint("main", __name__, template_folder='templates')


##########################################
#           Main Routes                  #
##########################################


@main.route('/')
def home():
    """Displays the homepage."""
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    """Create a new post"""
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(
            title=form.title.data,
            author=current_user,
            body=form.body.data
        )

        db.session.add(new_post)
        db.session.commit()
        post_id = new_post.id

        flash('New post was created successfully.')

        return redirect(url_for('main.post_detail', post_id=post_id))
    return render_template('new_post.html', form=form)


@main.route('/post/<post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.query.get(post_id)

    form = CommentForm()
    if form.validate_on_submit():

        if not current_user.is_authenticated:
            flash('Please login to comment.')
            return redirect(url_for('auth.login'))

        new_comment = Comment(
            body=form.body.data,
            author=current_user,
            post_id=post_id
        )

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.post_detail', post_id=post_id))

    return render_template('post_detail.html', post=post, form=form)


@main.route('/feed')
@login_required
def feed():
    posts = Post.query.all()

    return render_template('feed.html', posts=posts)
