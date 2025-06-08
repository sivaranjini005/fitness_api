from fastapi import HTTPException
from app.models import Booking, Class
from app.schemas import BookingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List


async def create_booking(
    db: AsyncSession, class_id: int, client_name: str, client_email: str
) -> BookingResponse:
    stmt = select(Class).where(Class.id == class_id)
    result = await db.execute(stmt)
    cls = result.scalars().first()

    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")

    if cls.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    # Create booking
    new_booking = Booking(
        class_id=class_id, client_name=client_name, client_email=client_email
    )
    cls.available_slots -= 1

    db.add(new_booking)
    await db.commit()
    await db.refresh(new_booking)

    return BookingResponse(
        id=new_booking.id,
        class_id=new_booking.class_id,
        client_name=new_booking.client_name,
        client_email=new_booking.client_email,
    )


async def get_bookings_by_email(db: AsyncSession, email: str) -> List[BookingResponse]:
    stmt = select(Booking).where(Booking.client_email == email)
    result = await db.execute(stmt)
    bookings = result.scalars().all()

    return [
        BookingResponse(
            id=b.id,
            class_id=b.class_id,
            client_name=b.client_name,
            client_email=b.client_email,
        )
        for b in bookings
    ]
