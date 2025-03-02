from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.crud import (get_notions, get_notion, create_one_notion,
                      update_put_one_notion,
                      update_patch_one_notion, delete_one_notion)
from core.db_helper import db_helper
from schemas import ReadNotion, CreateNotion, UpdateNotion

router = APIRouter()


@router.get('/', response_model=List[ReadNotion])
async def get_notions_view(session: AsyncSession = Depends(db_helper.session_getter)):
    queryset_of_notions = await get_notions(session=session)
    return queryset_of_notions


@router.get('/{pk}', response_model=ReadNotion)
async def get_one_notion_view(pk: int, session: AsyncSession = Depends(db_helper.session_getter)):
    notion = await get_notion(pk=pk, session=session)
    return notion


@router.post('/', response_model=ReadNotion)
async def create_new_notion_view(create_notion: CreateNotion,
                                 session: AsyncSession = Depends(db_helper.session_getter)):
    notion = await create_one_notion(session=session, create_notion=create_notion)
    return notion


@router.put('/{pk}', response_model=ReadNotion)
async def update_notion_view(pk: int, update_notion: CreateNotion,
                             session: AsyncSession = Depends(db_helper.session_getter)):
    notion = await update_put_one_notion(pk=pk, update_notion=update_notion, session=session)
    return notion


@router.patch('/{pk}', response_model=ReadNotion)
async def patch_notion_view(pk: int, patch_notion: UpdateNotion,
                            session: AsyncSession = Depends(db_helper.session_getter)):
    notion = await update_patch_one_notion(pk=pk, patch_notion=patch_notion, session=session)
    return notion


@router.delete('/{pk}')
async def delete_notion_view(pk: int, session: AsyncSession = Depends(db_helper.session_getter)):
    notion = await delete_one_notion(pk=pk, session=session)
    return {"был удален: ": notion}
