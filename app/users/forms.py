from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email, NumberRange

class LoginForm(Form):
  email = TextField('Email address', [Required(), Email()])
  password = PasswordField('Password', [Required()])

class RegisterForm(Form):
  name = TextField([Required()])
  email = TextField('Email address', [Required(), Email()])
  password = PasswordField('Password', [Required()])
  confirm = PasswordField('Repeat Password', [
      Required(),
      EqualTo('password', message='Passwords must match')
      ])
  accept_tos = BooleanField('I accept the TOS', [])
  accno = TextField()
  #recaptcha = RecaptchaField()
  
class ItemForm(Form):
  iname = TextField('Item Name', [Required()])
  idesc = TextField('Item Description')
  icost = TextField('Item Cost')
  ilink = TextField('Item Link')
  ipriority = TextField('Item Priority',[NumberRange(min=0)])
  iminbal = TextField('Minimum Balance Required to purchase',[Required(), NumberRange(min=0)])