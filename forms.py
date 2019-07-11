from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
	username=StringField("username", validators=[DataRequired(), Length(min=5,max=15)])
	email=StringField("email", validators=[DataRequired(), Email()])
	password=PasswordField("password", validators=[DataRequired()])
	confirm_password=PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField("Sign up")

class LoginForm(FlaskForm):
	email=StringField("email", validators=[DataRequired(), Email()])
	password=PasswordField("Password", validators=[DataRequired()])
	remember=BooleanField("Remember me")
	submit=SubmitField("Login")
	