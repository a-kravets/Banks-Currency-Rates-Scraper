import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()


class Bank(db.Model):
    __tablename__ = "banks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)




class Rate(db.Model):
    __tablename__ = "rates"
    id = db.Column(db.Integer, primary_key=True)
    usd_buy = db.Column(db.Float, nullable=True)
    usd_sell = db.Column(db.Float, nullable=True)
    eur_buy = db.Column(db.Float, nullable=True)
    eur_sell = db.Column(db.Float, nullable=True)
    date = db.Column(db.Date, nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey("banks.id"), nullable=False)
   
#db.create_all()