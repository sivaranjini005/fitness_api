from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import BookingRequest, BookingResponse
from app.services import booking_service
from app.logger import logger

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post(
    "/book/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED
)
async def book_class(request: BookingRequest, db: AsyncSession = Depends(get_db)):
    """
    Book a class for a client.

    Args:
        request (BookingRequest): Booking request data including class ID, client name, and email.
        db (AsyncSession): Database session dependency.

    Returns:
        BookingResponse: The created booking object.

    Raises:
        HTTPException: If the booking fails due to business logic or internal error.
    """
    logger.info(
        f"Booking request received: class_id={request.class_id}, email={request.client_email}"
    )

    try:
        booking = await booking_service.create_booking(
            db, request.class_id, request.client_name, request.client_email
        )

        logger.info(f"Booking successful: booking_id={booking.id}")

        return booking

    except HTTPException as e:
        logger.warning(f"Booking failed: {e.detail}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during booking: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/", response_model=list[BookingResponse])
async def get_bookings(email: str, db: AsyncSession = Depends(get_db)):
    """
    Retrieve all bookings for a given client email.

    Args:
        email (str): The client's email address to filter bookings.
        db (AsyncSession): Database session dependency.

    Returns:
        list[BookingResponse]: A list of bookings associated with the provided email.

    Raises:
        HTTPException: If fetching bookings fails.
    """
    logger.info(f"Fetching bookings for email: {email}")
    try:
        bookings = await booking_service.get_bookings_by_email(db, email)
        logger.info(f"Total bookings found: {len(bookings)} for {email}")
        return bookings
    except Exception as e:
        logger.error(f"Failed to fetch bookings for {email}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
