from .database import Base
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import configure_mappers


class GenericData(AbstractConcreteBase, Base):
    name = Column(String)
    timestamp = Column(DATETIME)
    optionaldata = Column(String)
    jsondata = Column(JSONB)
    uuid = Column(UUID, primary_key=True, index=True)


class GPS(GenericData):
    __tablename__ = "gps"
    __mapper_args__ = {
        'polymorphic_identity': 'gps',
        'concrete': True
    }


class SomeOtherData(GenericData):
    __tablename__ = "accumax"
    __mapper_args__ = {
        'polymorphic_identity': 'accumax',
        'concrete': True
    }

configure_mappers()
