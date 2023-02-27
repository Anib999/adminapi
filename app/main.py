from fastapi import FastAPI
from .routers import client, general, management, sales

app = FastAPI(swagger_ui_parameters={'defaultModelswExpandDepth': -1})

app.include_router(client.router)
app.include_router(general.router)
app.include_router(management.router)
app.include_router(sales.router)

@app.get('/')
async def index():
    return {'message': 'Welcome to Admin Dashboard API'}