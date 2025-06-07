from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models import Class, Booking


async def get_class_by_id(db: AsyncSession, class_id: int):
    result = await db.execute(select(Class).where(Class.id == class_id))
    return result.scalar_one_or_none()


async def create_booking(db: AsyncSession, class_id: int, name: str, email: str):
    fitness_class = await get_class_by_id(db, class_id)
    if not fitness_class:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No available slots")

    new_booking = Booking(class_id=class_id, client_name=name, client_email=email)
    db.add(new_booking)

    # Reduce slot count
    fitness_class.available_slots -= 1

    await db.commit()
    await db.refresh(new_booking)
    return new_booking


async def get_bookings_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(Booking).where(Booking.client_email == email))
    return result.scalars().all()
