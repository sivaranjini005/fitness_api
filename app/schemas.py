from datetime import datetime
from pydantic import BaseModel, EmailStr


class ClassResponse(BaseModel):
    """
    Schema representing a fitness class response.

    Attributes:
        id (int): Unique identifier of the class.
        name (str): Name of the class.
        instructor (str): Instructor's name.
        start_time (datetime): When the class begins.
        available_slots (int): Number of remaining slots for booking.
    """

    id: int
    name: str
    instructor: str
    start_time: datetime
    available_slots: int

    model_config = {"from_attributes": True}


class BookingRequest(BaseModel):
    """
    Schema for creating a booking.

    Attributes:
        class_id (int): ID of the class to book.
        client_name (str): Full name of the client.
        client_email (EmailStr): Valid email address of the client.
    """

    class_id: int
    client_name: str
    client_email: EmailStr

    model_config = {"from_attributes": True}


class BookingResponse(BookingRequest):
    """
    Schema for returning booking information to the client.

    Extends:
        BookingRequest

    Additional Attributes:
        id (int): Unique booking ID.
    """

    id: int

    model_config = {"from_attributes": True}
