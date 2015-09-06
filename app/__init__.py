from flask import Flask, render_template, request,session, redirect, flash,url_for
import os
import sys
from app.users.forms import RegisterForm, LoginForm
#from app.users.models import User
from app.users.decorators import requires_login
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import check_password_hash, generate_password_hash
app = Flask(__name__)
app.config.from_object('config')
from app.users import constants as USER

db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)
    accno = db.Column(db.Integer, default=0)
    balance = db.Column(db.Integer, default=0)

def __init__(self, name=None, email=None, password=None):
  self.name = name
  self.email = email
  self.password = password

def getStatus(self):
  return USER.STATUS[self.status]

def getRole(self):
  return USER.ROLE[self.role]

def __repr__(self):
  return '<User %r>' % (self.name)



class UserData(db.Model):
  
  __tablename__ = 'users_data'
  id = db.Column(db.Integer)
  item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  item_name = db.Column(db.String(100))
  item_desc = db.Column(db.String(120))
  item_cost = db.Column(db.Integer)
  item_link = db.Column(db.String(200),default="")
  item_priority = db.Column(db.Integer)
  item_minbal =db.Column(db.Integer)
  
  
def __init__(self):
  self.id = id
  self.item_name = item_id
  self.item_desc = item_desc 
  self.item_cost = item_cost
  self.item_link = item_link
  self.item_priority = item_priority
  self.item_minbal= item_minbal
    ########################
    # Configure Secret Key #
    ########################
def install_secret_key(app, filename='secret_key'):
       # """Configure the SECRET_KEY from a file
       # in the instance directory.

       # If the file does not exist, print instructions
      #  to create it from a shell with a random key,
      #  then exit.
     #   """
  filename = os.path.join(app.instance_path, filename)

  try:
    app.config['SECRET_KEY'] = open(filename, 'rb').read()
  except IOError:
    print('Error: No secret key. Create it with:')
    full_path = os.path.dirname(filename)
    if not os.path.isdir(full_path):
      print('mkdir -p {filename}'.format(filename=full_path))
    print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
    sys.exit(1)

  #if not app.config['DEBUG']:
    install_secret_key(app)


@app.route("/",methods=['GET', 'POST'])
def index():
  form = RegisterForm(request.form)
  
  if form.validate_on_submit():
        # create an user instance not yet stored in the database
    user = User(name=form.name.data, email=form.email.data, \
        password=generate_password_hash(form.password.data), accno=form.accno.data)
        # Insert the record in our database and commit it
    db.session.add(user)
    db.session.commit()
        # Log the user in, as he now has an id
    session['user_id'] = user.id

        # flash will display a message to the user
    flash('Thanks for registering')
    print "Registered Successfully"
    db.session.close()
        # redirect user to the 'home' method of the user module.
    return redirect(url_for('users.home'))
  print form.errors
  
  
  form2 = LoginForm(request.form)
      # make sure data are valid, but doesn't validate password is right
  if form2.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
        # we use werzeug to validate user's password
    if user and check_password_hash(user.password, form.password.data):
          # the session can't be modified as it's signed, 
          # it's a safe place to store the user id
      session['user_id'] = user.id
      flash('Welcome %s' % user.name)
      #window.top.location.href= url_for('users.home')
      return redirect(url_for('users.home'))
    flash('Wrong email or password', 'error-message')
    
    
    
  return render_template('index.html',form=form)
  
  
@app.errorhandler(404)
def not_found(error):
  return render_template('index.html'), 404

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)
