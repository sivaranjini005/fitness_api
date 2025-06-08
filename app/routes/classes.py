from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.database import get_db
from app.models import Class
from app.schemas import ClassResponse

router = APIRouter(prefix="/classes", tags=["classes"])


@router.get("/", response_model=List[ClassResponse])
async def get_classes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Class).order_by(Class.start_time))
    classes = result.scalars().all()
    return classes
