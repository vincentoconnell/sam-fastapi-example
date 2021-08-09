from fastapi import APIRouter
from .endpoints.example import router as example_router
from .endpoints.gps import router as gps_router


router = APIRouter()
router.include_router(example_router)
router.include_router(gps_router)
