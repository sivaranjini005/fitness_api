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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Class not found"
        )
    if fitness_class.available_slots <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No available slots"
        )

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


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models import Class, Booking
from typing import Optional, List


async def get_class_by_id(db: AsyncSession, class_id: int) -> Optional[Class]:
    """
    Retrieve a class by its ID.

    Args:
        db (AsyncSession): The async database session.
        class_id (int): ID of the class to fetch.

    Returns:
        Optional[Class]: The class instance if found, otherwise None.
    """
    result = await db.execute(select(Class).where(Class.id == class_id))
    return result.scalar_one_or_none()


async def create_booking(
    db: AsyncSession, class_id: int, client_name: str, client_email: str
) -> Booking:
    """
    Create a new booking for a given class.

    Args:
        db (AsyncSession): The async database session.
        class_id (int): The ID of the class to be booked.
        client_name (str): Name of the client making the booking.
        client_email (str): Email of the client making the booking.

    Returns:
        Booking: The newly created booking instance.

    Raises:
        HTTPException: If the class is not found or has no available slots.
    """
    fitness_class = await get_class_by_id(db, class_id)
    if not fitness_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found",
        )

    if fitness_class.available_slots <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No available slots",
        )

    # Create and add the booking
    new_booking = Booking(
        class_id=class_id, client_name=client_name, client_email=client_email
    )
    db.add(new_booking)

    # Decrement the slot count
    fitness_class.available_slots -= 1

    # Commit and refresh booking instance
    await db.commit()
    await db.refresh(new_booking)
    return new_booking


async def get_bookings_by_email(db: AsyncSession, email: str) -> List[Booking]:
    """
    Retrieve all bookings for a specific client by email.

    Args:
        db (AsyncSession): The async database session.
        email (str): The email address of the client.

    Returns:
        List[Booking]: A list of bookings associated with the client.
    """
    result = await db.execute(select(Booking).where(Booking.client_email == email))
    return result.scalars().all()
