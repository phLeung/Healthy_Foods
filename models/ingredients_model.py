import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ingredients.db')

db = SQLAlchemy(app)
#declaration of ingredients model
class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(95), unique=True, nullable=False)

    def __repr__(self):
        return '<Ingredient %r>' % self.name
