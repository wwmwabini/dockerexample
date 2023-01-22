from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
	firstname = StringField('First Name', validators=[DataRequired()])
	email = EmailField('Email', validators=[DataRequired()])
	save = SubmitField('Save Changes')