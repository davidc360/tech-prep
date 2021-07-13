from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, FloatField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError


class PostForm(FlaskForm):
    """Form to create a post"""
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=1, max=80)])
    body = StringField('Body',
                       validators=[Length(min=0, max=40000)])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """Form to create a comment"""
    body = StringField('Add a comment',
                       validators=[DataRequired(), Length(min=0, max=40000)])
    submit = SubmitField('Submit')
