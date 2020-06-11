import os

from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import func
from banks import *
from models import *
from datetime import date
from datetime import datetime

app = Flask(__name__)

#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    for usd_buy, usd_sell, eur_buy, eur_sell, date, bank_id in banks:
        try: #we need to check if the date exists in the column at all for the first timers
            existing_date = Rate.query.filter_by(bank_id = bank_id).order_by(Rate.date.desc()).first()
            if existing_date.date.strftime("%Y-%m-%d") != date and datetime.now().strftime("%H:%M:%S") >= '09:30:00':
                bank_info = Rate(usd_buy=usd_buy, usd_sell=usd_sell, eur_buy=eur_buy, eur_sell=eur_sell, date=date, bank_id=bank_id)
                db.session.add(bank_info)
                db.session.commit()
        except: #if it fails (happens in the 1st time), we assume we may add
                bank_info = Rate(usd_buy=usd_buy, usd_sell=usd_sell, eur_buy=eur_buy, eur_sell=eur_sell, date=date, bank_id=bank_id)
                db.session.add(bank_info)
                db.session.commit()

    rates = db.session.query(Rate, Bank).filter(and_(Rate.bank_id == Bank.id, Rate.date == datetime.today().strftime("%Y-%m-%d"))).order_by(Bank.name.asc()).all()

    stat = db.session.query(func.max(Rate.usd_buy).label("usd_buy_max"), 
                    func.max(Rate.usd_sell).label("usd_sell_max"),
                    func.avg(Rate.usd_buy).label("usd_buy_avg"),
                    func.avg(Rate.usd_sell).label("usd_sell_avg"),
                    func.min(Rate.usd_buy).label("usd_buy_min"),
                    func.min(Rate.usd_sell).label("usd_sell_min"),
                    func.max(Rate.eur_buy).label("eur_buy_max"),
                    func.max(Rate.eur_sell).label("eur_sell_max"),
                    func.avg(Rate.eur_buy).label("eur_buy_avg"),
                    func.avg(Rate.eur_sell).label("eur_sell_avg"),
                    func.min(Rate.eur_buy).label("eur_buy_min"),
                    func.min(Rate.eur_sell).label("eur_sell_min"),
                    ).filter(Rate.date == datetime.today().strftime("%Y-%m-%d"))

    stat_res = stat.one()
 
    return render_template("index.html", rates=rates, existing_date=existing_date, stat_res=stat_res)

@app.route("/analytics")
def analytics():
    data = db.session.query(Bank, Rate).filter(Rate.bank_id == Bank.id).order_by(Rate.bank_id).all()
    stat = db.session.query(func.max(Rate.usd_buy).label("usd_buy_max"), 
                    func.max(Rate.usd_sell).label("usd_sell_max"),
                    func.avg(Rate.usd_buy).label("usd_buy_avg"),
                    func.avg(Rate.usd_sell).label("usd_sell_avg"),
                    func.min(Rate.usd_buy).label("usd_buy_min"),
                    func.min(Rate.usd_sell).label("usd_sell_min"),
                    func.max(Rate.eur_buy).label("eur_buy_max"),
                    func.max(Rate.eur_sell).label("eur_sell_max"),
                    func.avg(Rate.eur_buy).label("eur_buy_avg"),
                    func.avg(Rate.eur_sell).label("eur_sell_avg"),
                    func.min(Rate.eur_buy).label("eur_buy_min"),
                    func.min(Rate.eur_sell).label("eur_sell_min"),
                    ).filter(Rate.date == datetime.today().strftime("%Y-%m-%d"))
    #qry = qry.group_by(Rate.eur_buy)
    res = stat.one()
    
    return render_template("analytics.html", res=res, data=data)


@app.route("/banks/<int:id>")
def bank(id):

    # Make sure bank exists.
    bank = Bank.query.get(id)
    if bank is None:
        return render_template("error.html", message="No such bank.")

    # Get all rates from specific bank.
    rates = db.session.query(Rate, Bank).filter(and_(Rate.bank_id == Bank.id, Rate.bank_id == id)).all()
 
    return render_template("bank.html", rates=rates)

