from fastapi import HTTPException, status
from app.models import Booking, Class
from app.schemas import BookingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List


async def create_booking(
    db: AsyncSession, class_id: int, client_name: str, client_email: str
) -> BookingResponse:
    """
    Create a new booking for a specified class if slots are available.

    Args:
        db (AsyncSession): The asynchronous database session.
        class_id (int): The ID of the class to book.
        client_name (str): The name of the client making the booking.
        client_email (str): The email of the client making the booking.

    Raises:
        HTTPException: If the class does not exist (404).
        HTTPException: If there are no available slots for the class (400).

    Returns:
        BookingResponse: The booking details including booking ID, class ID, client name, and email.
    """
    stmt = select(Class).where(Class.id == class_id)
    result = await db.execute(stmt)
    cls = result.scalars().first()

    if not cls:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Class not found"
        )

    if cls.available_slots <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No slots available"
        )

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
    """
    Retrieve all bookings associated with a given client email.

    Args:
        db (AsyncSession): The asynchronous database session.
        email (str): The email address of the client whose bookings are to be fetched.

    Returns:
        List[BookingResponse]: A list of booking details matching the provided email.
    """
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
