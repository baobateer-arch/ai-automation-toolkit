from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router
from app.api.upload import router as upload_router
from app.api.auth import router as auth_router
from app.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="Contract Risk AI", lifespan=lifespan)
app.include_router(router)
app.include_router(upload_router)
app.include_router(auth_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
