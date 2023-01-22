from users import app, db
from users.models import Users
from flask import render_template

@app.route('/')
def show():

	users = Users.query.all()

	return render_template('show.html', users=users)