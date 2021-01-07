from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm,CSRFProtect
from flask_mail import Mail

app=Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offerzone.db'

db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'offerzoneofferzone@gmail.com'
app.config['MAIL_PASSWORD'] = 'offerzone123'
app.config['MAIL_DEFAULT_SENDER'] = 'offerzone123'
mail = Mail(app)


from OfferZone import routes

