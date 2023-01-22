from register import app, db
from register.forms import RegistrationForm
from flask import render_template, redirect, url_for
from register.models import Users


@app.route('/', methods=['GET', 'POST'])
def register():

	form = RegistrationForm()

	if form.validate_on_submit():

		record = Users(firstname=form.firstname.data, email=form.email.data)
		db.session.add(record)
		db.session.commit()

		return redirect(url_for('register'))


	return render_template('register.html', form=form)