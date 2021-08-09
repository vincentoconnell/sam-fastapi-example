# import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import router as api_router
from app.core.config import API_V1_STR, PROJECT_NAME


app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    root_path="/prod/api"
)


app.include_router(api_router, prefix=API_V1_STR)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS", "DELETE", "PUT"],
    allow_headers=[
        "Access-Control-Allow-Headers",
        "Origin",
        "Accept",
        "X-Requested-With",
        "Content-Type",
        "Access-Control-Request-Method",
        "Access-Control-Request-Headers",
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Methods"
        "Authorization",
        "X-Amz-Date",
        "X-Api-Key",
        "X-Amz-Security-Token"
    ]
)


@app.get("/ping")
def pong():
    return {"ping": "pong!"}

# @app.on_event("startup")
# async def startup():
#     await db.database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await db.database.disconnect()

handler = Mangum(app, enable_lifespan=False)

# if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8080)

