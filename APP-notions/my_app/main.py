import sys
from contextlib import asynccontextmanager
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from api import notions_router
from core.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    sys.stderr.write(f'start app {datetime.now()}')
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all())
    yield
    await db_helper.dispose()
    sys.stderr.write(f'finished app {datetime.now()}')


app = FastAPI(lifespan=lifespan)
app.include_router(notions_router)
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
