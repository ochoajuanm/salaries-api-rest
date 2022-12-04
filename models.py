from flask_sqlalchemy import SQLAlchemy
from extensions import db


class Salary(db.Model):
    __tablename__ = "Salaries"

    id = db.Column(db.Integer, primary_key=True)
    employeename = db.Column(db.String(200), nullable=False)
    jobtitle = db.Column(db.String(200), nullable=False)
    basepay = db.Column(db.String(200), nullable=False)
    overtimepay = db.Column(db.String(200), nullable=False)
    otherpay = db.Column(db.String(200), nullable=False)
    benefits = db.Column(db.String(200), nullable=False)
    totalpay = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    totalpaybenefits = db.Column(
        db.Numeric(
            precision=10,
            scale=2),
        nullable=False)
    year = db.Column(db.Numeric(precision=10, scale=0), nullable=False)
    notes = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    agency = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
