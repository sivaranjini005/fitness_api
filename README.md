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



---

## ⚙️ Setup Instructions

### 1. Clone the Repository

<pre>
git clone https://github.com/sivaranjini005/fitness_api.git
cd fitness_api</pre>

### 2. Create and Activate Virtual Environment

<pre>python -m venv venv
venv\Scripts\activate  # On Windows
# or on macOS/Linux
# source venv/bin/activate</pre>

### 3. Install Dependencies
<pre>
pip install -r requirements.txt</pre>

### 🌱 Seeding the Database
#### To insert sample classes into the database:
<pre>
python seed_data.py</pre>

### 🚀 Run the Application
<pre>
  uvicorn app.main:app --reload
</pre>

#### API Base URL: http://127.0.0.1:8000
#### Swagger Docs: http://127.0.0.1:8000/docs

### 🧪 Running Tests
#### Make sure the app is not running while running tests, since test cases create their own instance:
<pre>
  pytest tests/test_classes.py
  pytest tests/test_booking.py
</pre>

### 📬 API Endpoints
#### GET /classes/
  * Description: List all fitness classes.
  * Response: JSON array with class info.

#### POST /bookings/book/

  * Description: Book a class using name, email and class ID.

Request Example:
<pre>
  {
  "client_name": "User"
  "client_email": "user@gmail.com",
  "class_id": 1
}
</pre>

  * Success: 201 Created
  * Failure: 400, 404, or 422

### 🧰 Technologies Used
  * FastAPI    -- Supports asynchronous programming
  * SQLAlchemy -- ORM
  * SQLite     -- Database 
  * Pydantic   -- Data validation
  * Pytest     -- Unit Testing
  * HTTPX      -- For async API testing

### 📬 Contact
For any questions, suggestions, or feedback, feel free to open an issue or reach out.
