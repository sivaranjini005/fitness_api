"""Database models for the fitness application."""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Class(Base):
    """Model representing fitness classes in the system."""

    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    instructor = Column(String, nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    available_slots = Column(Integer, default=0, nullable=False)

    bookings = relationship("Booking", back_populates="fitness_class")


class Booking(Base):
    """Model representing class bookings made by clients."""

    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    booked_at = Column(DateTime(timezone=True), server_default=func.now())

    fitness_class = relationship("Class", back_populates="bookings")
