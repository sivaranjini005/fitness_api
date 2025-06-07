# 🧘‍♀️ Fitness Class Booking API

This is a FastAPI-based backend application for managing fitness class bookings. It allows clients to view available classes and book them, with automatic slot management.

## 🚀 Features

- View available fitness classes
- Book a class with limited slots
- Validations to prevent overbooking
- Integrated with SQLite via SQLAlchemy
- Pydantic models for data validation
- Includes seed data for testing/demo
- Tested with `pytest`

---

## 📁 Project Structure
<pre lang="markdown">

fitness_api/
  ├──app/
            ├──__init__.py
            ├──repositories/
                         ├──__init__.py
                         ├──booking_repo.py
            ├──routes/
                         ├──__init__.py
                         ├──bookings.py
                         ├──classes.py
             ├──services/
                          ├──__init__.py
                          ├──booking_service.py
             ├──database.py
             ├──logger.py
             ├──main.py
             ├──schemas.py
             ├──models.py
    ├──tests/
             ├──test_classes.py
             ├──test_booking.py
    ├──run.py
    ├──seed_data.py
    ├──requirements.txt
    ├──.gitignore
    ├──.env
    ├──README.md
</pre>

