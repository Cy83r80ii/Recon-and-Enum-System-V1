from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True)
    target = Column(String)
    mode = Column(String)
    created = Column(DateTime, default=datetime.utcnow)


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    scan_id = Column(Integer)
    type = Column(String)
    severity = Column(String)
    url = Column(String)
