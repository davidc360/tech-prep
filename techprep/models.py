from sqlalchemy_utils import URLType
from flask_login import UserMixin
from techprep import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    date_created = db.Column(db.DateTime, nullable=False)
    last_active = db.Column(db.DateTime, nullable=False)

    posts = db.relationship('Post', back_populates='author')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.String(40000), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', back_populates='posts')

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
