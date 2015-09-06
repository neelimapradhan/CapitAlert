from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for,Flask
from werkzeug import check_password_hash, generate_password_hash
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String
from app import db
from app.users.forms import RegisterForm, LoginForm, ItemForm
#from app.users.models import User
from app import User, UserData
from app.users.decorators import requires_login
from app.capitalData import *

mod = Blueprint('users', __name__, url_prefix='/users')
#engine = create_engine('sqlite:////app.db')
#metadata = MetaData()
#metadata.create_all(bind=engine)

@mod.route('/me/', methods=['GET', 'POST'])
@requires_login
def home():
  id=0
  balance_current=get_Balance(id)
  print "home balance is " + str(balance_current)
  myid= session['user_id']
  form = LoginForm(request.form)
  user = User.query.filter_by(id=myid).update(dict(balance=balance_current))
  db.session.commit() 
  
  r=UserData.query.filter_by(id=myid).all()
  item_names=[]
  item_descs=[]
  item_costs=[]
  item_links=[]
  item_prioritys=[]
  item_minbals=[]
  item_ids=[]
  global count
  count=0
  for items in r:
    item_ids.append(items.item_id)
    item_names.append(items.item_name)
    if items.item_desc==' ':
      item.descs.append("No Description")
    else:  
      item_descs.append(items.item_desc)
    item_costs.append(items.item_cost)
    item_links.append(items.item_link)
    item_prioritys.append(items.item_priority)
    item_minbals.append(items.item_minbal)
    count=count+1
  print item_ids
  print item_names
  print item_descs
  print item_costs
  print item_links
  print item_prioritys
  print item_minbals
			    
			    
  return render_template("users/profile.html", user=g.user,count=count,item_names=item_names,item_descs=item_descs,item_costs=item_costs,item_links=item_links,item_prioritys=item_prioritys,item_minbals=item_minbals, item_ids=item_ids)
  
@mod.route('/me/add_item', methods=['GET', 'POST'])  
@requires_login    
def add_item():
  myid= session['user_id']
  form3 = ItemForm(request.form)
  if request.method == "POST" and form3.validate_on_submit():
    flash("Success")
    useritem = UserData(id=myid, item_name=form3.iname.data,item_desc=form3.idesc.data, item_cost=form3.icost.data,item_link=form3.ilink.data,item_priority=form3.ipriority.data, item_minbal=form3.iminbal.data)
    # Insert the record in our database and commit it
    db.session.add(useritem)
    db.session.commit()
    print "Item added successfully"
  return render_template("users/add_item.html", user=g.user,form3=form3)

@mod.route('/me/delete_item/<id>', methods=['GET', 'POST'])  
@requires_login    
def delete_item(id):
  user = UserData.query.get(id)
  db.session.delete(user)
  db.session.commit()
  print "Item successfully deleted"
  return redirect(url_for('users.home'))

@mod.before_request
def before_request():
     # "pull user's profile from the database before every request are treated"
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])

@mod.route('/login/', methods=['GET', 'POST'])
def login():
#  Login form
  form = LoginForm(request.form)
      # make sure data are valid, but doesn't validate password is right
  if form.validate_on_submit():
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
    
  return render_template("users/login.html", form=form)

@mod.route('/register/', methods=['GET', 'POST'])
def register():
    #  Registration Form
  form = RegisterForm(request.form)
  if form.validate_on_submit():
        # create an user instance not yet stored in the database
    user = User(name=form.name.data, email=form.email.data, \
        password=generate_password_hash(form.password.data))
        # Insert the record in our database and commit it
    db.session.add(user)
    db.session.commit()

        # Log the user in, as he now has an id
    session['user_id'] = user.id

        # flash will display a message to the user
    flash('Thanks for registering')
        # redirect user to the 'home' method of the user module.
    return redirect(url_for('users.home'))
  return render_template("users/register.html", form=form)