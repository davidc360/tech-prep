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

    recipes = db.relationship('Recipe', backref='user')
    meals = db.relationship('Meal', backref='user')


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)
