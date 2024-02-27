from flask import Flask
import os
from flask import Flask,  render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

peach = Flask(__name__)


basedirectory = os.path.abspath(os.path.dirname(__file__))

peach.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://leigh:bezalel84@host:5432/tunzamalie"
peach.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(peach)

migrate = Migrate(peach, db, command='migrate')


@peach.route("/")
def home():
    return  '<h1>Tunza Mali</h1>'

