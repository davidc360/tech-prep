from flask import Blueprint, request, render_template, redirect, url_for, flash

main = Blueprint("main", __name__, template_folder='templates')

from techprep import db
from techprep.main.forms import PostForm

from flask_login import login_required, current_user
##########################################
#           Main Routes                  #
##########################################


@main.route('/')
def home():
    """Displays the homepage."""
    return render_template('home.html')

@main.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    """Create a new post"""
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(
            title = form.title.data,
            author = current_user.id,
            body = form.body.data
        )
        post_id = new_post.id
        db.session.add(new_post)
        db.session.commit()
        flash('New post was created successfully.')

        return redirect(url_for('main.post_detail', post_id=post_id))
    return render_template('new_post.html', form=form)

@main.route('/post/<post_id>')
def post_detail(post_id):
    return render_template('post_detail.html')