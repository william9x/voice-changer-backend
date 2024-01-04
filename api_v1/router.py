from fastapi import APIRouter

from api_v1.routes import health, infer

router = APIRouter(prefix='/v1')

router.include_router(health.router)
router.include_router(infer.router)
