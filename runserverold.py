import os
import sys
from flask import Flask, render_template
from flask_wtf import Form
from wtforms.fields import TextField, PasswordField, FileField
from wtforms.validators import DataRequired, Email
from wtforms.ext.appengine.db import model_form
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
from flask import Blueprint, render_template, abort

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
db = SQLAlchemy(app)
from app.users.views import mod as usersModule



app.register_blueprint(usersModule)  

@app.route("/")
def main():
	return "hello world yoyo"

class MyForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.name = None
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True    

#@app.before_request
#def csrf_protect():
    #if request.method == "POST":
        #token = session.pop('_csrf_token', None)
        #if not token or token != request.form.get('_csrf_token'):
            #abort(403)

#def generate_csrf_token():
    #if '_csrf_token' not in session:
        #session['_csrf_token'] = some_random_string()
    #return session['_csrf_token']

#app.jinja_env.globals['csrf_token'] = generate_csrf_token      

@app.route('/submit', methods=('GET', 'POST'))



def submit():
    form = MyForm(csrf_enabled=False)
    if form.validate_on_submit():
        return redirect('/')
    return render_template('index.html', form=form)
  
class PhotoForm(Form):
    photo = FileField('Your photo')

@app.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save('uploads/' + filename)
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)
  

if __name__ == "__main__":
	app.run(debug=True)
	