"""funny komodo database table definitions"""

from datetime import datetime, timezone

from sqlalchemy import Column
from sqlalchemy import BigInteger, Boolean, Date, DateTime, Float, Integer, String

from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declared_attr

mapper_registry = registry()

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Fortune(Base):
    """fortune table definition"""

    __tablename__ = "fortune"

    id = Column(Integer, primary_key=True)
    eval_flag = Column(Boolean)
    mask = Column(Integer)
    uuid = Column(String)
    message = Column(String)

    def __init__(self, eval_flag, mask, uuid, message):
        self.eval_flag = eval_flag
        self.mask = mask
        self.uuid = uuid
        self.message = message

    def __repr__(self):
        return f"<fortune({self.id}, {self.mask}, {self.uuid})>"
