from datetime import datetime
from pydantic import BaseModel, EmailStr


# this defines how client get response when accessing the classes
class ClassResponse(BaseModel):
    id: int
    name: str
    instructor: str
    start_time: datetime
    available_slots: int

    model_config = {"from_attributes": True}


class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

    model_config = {"from_attributes": True}


class BookingResponse(BookingRequest):
    id: int

    model_config = {"from_attributes": True}
