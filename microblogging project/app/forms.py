from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, data_required, ValidationError, Email

from app.models import User


class Login_form(FlaskForm):
    username = StringField('username', validators=[
        data_required(),
    ])
    password = PasswordField('password', validators=[
        data_required(),
    ])
    submit = SubmitField()
    remember_me = BooleanField('remember me')


class Registration_form(FlaskForm):
    username = StringField('username', validators=[
        data_required(),
    ])
    email = EmailField('email', validators=[
        DataRequired(),
        Email(),
    ])
    password = PasswordField('password', validators=[
        data_required(),
    ])
    submit = SubmitField()

    def validate_email(self, email):
        myuser = User.query.filter(User.user_email == email.data).first()
        if myuser is not None:
            raise ValidationError(
                'Please enter different email. email is already used.')


class Edit_about_me(FlaskForm):
    about_me = StringField('about_me')
    submit = SubmitField()
