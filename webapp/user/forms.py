from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
	username = StringField('Name user:', validators=[DataRequired()], render_kw={"class": "form-control"})
	password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
	remember_me = BooleanField('Save me', render_kw={"class": "romm_check_input"}, default=True)
	submit = SubmitField('Send', render_kw={"class": "btn btn-primary"})