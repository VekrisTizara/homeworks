import os
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declared_attr
from flask_sqlalchemy import SQLAlchemy

PG_CONN_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "postgresql+psycopg2://app:password@localhost/plants"

db = SQLAlchemy()

class Plant(db.Model):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    type = Column(String(32), nullable=True)
