from ProjectEuler.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect
from ProjectEuler.Models import User, Post
from ProjectEuler import app, db, bcrypt

posts = [
	{
		'title' : 'ProjectEuler Flask Project',
		'author' : 'Pragya, Udit, Vanshika',
		'content' : 'First content',
		'date' : '21 June 2019'
	},

	# {
	# 	'title' : 'BP 2',
	# 	'author' : 'Tanya boi',
	# 	'content' : 'Second content',
	# 	'date' : '20 June 2019'
	# }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# hashed_pw=form.password.data
		hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.data, email=form.email.data, password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}! You can now log in.', 'success')
		return redirect(url_for('login'))
	return render_template('registration.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		if form.email.data=='abc@gmail.com' and form.password.data=='password':
			flash(f"Logged in as {form.email.data}!", 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Unsuccessful Login. Check username and password.', 'danger')
	return render_template('login.html', title='Login', form=form)
