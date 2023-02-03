from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class SignupForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField('Input your Name', validators=[DataRequired()])
    password = PasswordField('Please input your Password', validators=[DataRequired(), EqualTo('password2', message = 'Password must match')])
    password2 = PasswordField('Confirm your Password', validators = [DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField("Email:", validators = [DataRequired(), Email()])
    password = PasswordField("Password:", validators =[DataRequired()])
    submit = SubmitField("Login")