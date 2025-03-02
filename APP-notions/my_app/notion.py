from typing import List

from fastapi import APIRouter
from schemas import ReadNotion


notions_router = APIRouter(prefix='/notions', tags=['notions'])

