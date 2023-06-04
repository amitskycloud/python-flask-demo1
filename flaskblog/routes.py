from flask import render_template , url_for, flash,redirect
from flaskblog.forms import RegistrationForm
from flaskblog import app
@app.route("/")
@app.route("/home")
def home(): 
  return  render_template("home.html")

@app.route("/register",methods=["GET","POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect('home')
  return render_template('register.html',title="Register" , form=form)

@app.route("/login")
def login():
  pass