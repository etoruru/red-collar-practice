from fastapi.routing import APIRouter
from web import recipe_router

api_router = APIRouter()


api_router.include_router(recipe_router.router, prefix='/recipes', tags=['recipes'])
