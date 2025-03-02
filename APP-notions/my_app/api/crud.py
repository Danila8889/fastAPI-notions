from fastapi import HTTPException, status
from sqlalchemy import select
from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Notion
from schemas import CreateNotion, UpdateNotion

exc = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not found notion')


async def get_notions(session: AsyncSession) -> Sequence[Notion]:
    stmt = select(Notion).order_by(Notion.id)
    notions = await session.scalars(stmt)
    return notions.all()


async def get_notion(pk: int, session: AsyncSession) -> Notion:
    stmt = select(Notion).where(Notion.id == pk)
    notion = await session.scalar(stmt)
    if not notion:
        raise exc
    return notion


async def create_one_notion(session: AsyncSession, create_notion: CreateNotion) -> Notion:
    notion = Notion(**create_notion.model_dump())
    session.add(notion)
    await session.commit()
    # await session.refresh()
    return notion


async def update_put_one_notion(pk: int, update_notion: CreateNotion, session: AsyncSession) -> Notion:
    stmt = select(Notion).where(Notion.id == pk)
    notion = await session.scalar(stmt)
    notion.network = update_notion.model_dump().get('network')
    await session.commit()
    return notion


async def update_patch_one_notion(pk: int, patch_notion: UpdateNotion, session: AsyncSession) -> Notion:
    stmt = select(Notion).where(Notion.id == pk)
    notion = await session.scalar(stmt)
    notion.network = patch_notion.model_dump().get('network', notion.network)
    await session.commit()
    return notion


async def delete_one_notion(pk: int, session: AsyncSession) -> Notion:
    stmt = select(Notion).where(Notion.id == pk)
    notion = await session.scalar(stmt)
    await session.delete(notion)
    await session.commit()
    return notion
