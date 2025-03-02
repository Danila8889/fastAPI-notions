from fastapi import APIRouter

from api.notion_views import router

notions_router = APIRouter(prefix='/notions', tags=['notions'])

notions_router.include_router(router=router)