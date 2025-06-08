from fastapi import FastAPI
from app.routes import classes, bookings

app = FastAPI()

app.include_router(classes.router)
app.include_router(bookings.router)


# Optional root route
@app.get("/")
def root():
    return {"message": "Welcome to the Fitness Studio Booking API"}
