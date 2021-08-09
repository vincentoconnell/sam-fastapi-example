from app.core import GPSDAO, schemas
from app.core.database import get_db, get_company_trucks
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from datetime import datetime


router = APIRouter()


@router.get("/gpstest", response_model=List[schemas.GPS])
async def gps_get_test(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if limit > 100:
        limit = 100
    gpses = GPSDAO.get_gps(db, offset=offset, limit=limit)
    return gpses


@router.get("/gps", response_model=List[schemas.GPS])
async def gps_get(
    startdate: datetime,
    enddate: datetime,
    id: str,
    offset: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    auth_data: List = Depends(get_data)
):
    if limit > 1000:
        limit = 1000

    name = None
    for authDict in auth_data:
        if authDict.get("id") == id:
            name = authDict.get("name")
    if id is None or name is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"No Object found for id={id}")

    gpses = GPSDAO.get_gps_by_date_range(db, startdate, enddate, name, offset=offset, limit=limit)
    return gpses
