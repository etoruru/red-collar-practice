from fastapi.routing import APIRouter
from web import unit_router

api_router = APIRouter()

api_router.include_router(unit_router.router, prefix='/units', tags=['units'])
