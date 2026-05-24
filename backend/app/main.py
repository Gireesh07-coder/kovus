from fastapi import FastAPI
from app.routes.analyze import router as analyze_router
from app.routes.incidents import router as incidents_router
from app.routes.stats import router as stats_router

app = FastAPI()

app.include_router(analyze_router)
app.include_router(incidents_router)
app.include_router(stats_router)


@app.get("/")
def home():
    return {"message": "Kovus API Running"}