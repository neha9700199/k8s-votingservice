from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

