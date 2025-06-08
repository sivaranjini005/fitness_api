"""
Main entry point for the Fitness Studio Booking API.
Initializes the FastAPI application and includes route modules.
"""

from fastapi import FastAPI
from app.routes import classes, bookings

# Initialize FastAPI app with metadata for documentation
app = FastAPI(
    title="Fitness Studio Booking API",
    version="1.0.0",
    description="An API to manage fitness class bookings, availability, and client schedules.",
)

# Include routers from route modules
app.include_router(classes.router)
app.include_router(bookings.router)


@app.get("/")
def root():
    """
    Root endpoint to verify the API is running.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome to the Fitness Studio Booking API"}
