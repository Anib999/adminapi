from fastapi import FastAPI
from . import models
from .routers import client, general, management, sales
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(swagger_ui_parameters={'defaultModelsExpandDepth': -1})

app.include_router(client.router)
app.include_router(general.router)
app.include_router(management.router)
app.include_router(sales.router)

@app.get('/')
async def index():
    return {'message': 'Welcome to Admin Dashboard API'}