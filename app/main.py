from fastapi import FastAPI
from app.routes import items, clock_in

app = FastAPI()

app.include_router(items.router, prefix="/api", tags=["Items"])
app.include_router(clock_in.router, prefix="/api", tags=["Clock-In Records"])

@app.get("/")
async def root():
    return {"message": "FastAPI CRUD application with MongoDB"}
