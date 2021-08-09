from typing import Optional
from datetime import datetime
from pydantic import BaseModel
import uuid as pyuuid


class GenericData(BaseModel):
    name: str
    timestamp: datetime
    optionaldata: Optional[str]
    jsondata: dict
    uuid: pyuuid.UUID


class GPS(GenericData):
    class Config:
        orm_mode = True


class SomeOtherData(GenericData):
    class Config:
        orm_mode = True
