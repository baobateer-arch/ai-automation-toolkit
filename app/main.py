from fastapi import FastAPI
from app.api.routes import router
from app.api.upload import router as upload_router

app = FastAPI(title="AI Automation Toolkit")
app.include_router(router)
app.include_router(upload_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
