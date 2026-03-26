from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from Backend.app.database.database import init_db
from Backend.app.api.game_router import router as game_router

app = FastAPI()

app.include_router(game_router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )