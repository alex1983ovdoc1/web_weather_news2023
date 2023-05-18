from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


class LoginForm(FlaskForm):
	username = StringField('Name user:', validators=[DataRequired()], render_kw={"class": "form-control"})
	password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
	remember_me = BooleanField('Save me', render_kw={"class": "romm_check_input"}, default=True)
	submit = SubmitField('Send', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
	username = StringField('Name user:', validators=[DataRequired()], render_kw={"class": "form-control"})
	email = StringField('Your email:', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
	password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
	password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
	submit = SubmitField('Send', render_kw={"class": "btn btn-primary"})	

	def validate_username(self, username):
		user_count = User.query.filter_by(username=username.data).count()
		if user_count > 0:
			raise ValidationError('User with this name was registered')

	def validate_email(self, email):
		user_count = User.query.filter_by(email=email.data).count()
		if user_count > 0:
			raise ValidationError('User with this email was registered')


