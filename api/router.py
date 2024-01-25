from fastapi import APIRouter

from api.routes import health, infer

api = APIRouter()
api.include_router(health.router)

api_v1 = APIRouter(prefix='/api/v1')
api_v1.include_router(infer.router)
