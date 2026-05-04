from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Email

import sqlalchemy as sqla
from app import db
from app.main.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()]) 
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Register')

    def validate_username(self, username):
       query = sqla.select(User).where(User.username == username.data)
       user = db.session.scalars(query).first()
       if user is not None:
           raise ValidationError('The username already exists! Please use a different username.')
       
    def validate_email(sef, email):
       query = sqla.select(User).where(User.email == email.data)
       user = db.session.scalars(query).first()
       if user is not None:
          raise ValidationError('The email already exists! Please use a different username.')

class LoginForm(FlaskForm):
   username = StringField('Username', validators = [DataRequired()]) 
   password = PasswordField('Password', validators = [DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')

