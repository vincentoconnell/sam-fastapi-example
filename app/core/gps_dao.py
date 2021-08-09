from sqlalchemy.orm import Session
from . import models
from datetime import datetime


def get_gps(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.GPS).order_by(models.GPS.timestamp).offset(offset).limit(limit).all()


def get_gps_by_date_range(db: Session, startdate: datetime, enddate: datetime, name: str, offset: int = 0, limit: int = 0):
    return db.query(models.GPS).filter(models.GPS.name == name)\
        .filter(models.GPS.timestamp < enddate)\
        .filter(models.GPS.timestamp > startdate).order_by(models.GPS.timestamp).offset(offset).limit(limit).all()
