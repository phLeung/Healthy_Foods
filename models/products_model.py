import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #suppress warnings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'products.db')

db = SQLAlchemy(app)
#declaration of product model
class Product(db.Model):
    product_id = db.Column(db.Integer,primary_key=True)
    product_name = db.Column(db.String(95),unique=True,nullable=False)
    product_collection = db.Column(db.String(95),nullable=False)
    product_ingredient_ids = db.Column(db.ARRAY(Integer),nullable=False)

    def __repr__(self):
        return '<Product name: {}><Product collection: {}>'.format(self.product_name,self.product_collection)
