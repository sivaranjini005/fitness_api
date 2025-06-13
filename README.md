# 🧘‍♀️ Fitness Class Booking API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org)
[![Tests](https://img.shields.io/badge/Tests-Passing-green)](tests)

This is a FastAPI-based backend application for managing fitness class bookings. It allows clients to view available classes and book them, with automatic slot management.

## 📑 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Project Structure](#-project-structure)
- [Setup Instructions](#%EF%B8%8F-setup-instructions)
- [Environment Variables](#-environment-variables)
- [API Documentation](#-api-documentation)
- [Error Handling](#-error-handling)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Monitoring and Logging](#-monitoring-and-logging)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [Changelog](#-changelog)
- [License](#-license)

## 🚀 Features

- View available fitness classes
- Book a class with limited slots
- Validations to prevent overbooking
- Integrated with SQLite via SQLAlchemy
- Pydantic models for data validation
- Includes seed data for testing/demo
- Tested with `pytest`

## 🔧 Prerequisites

- Python 3.8 or higher
- pip package manager
- SQLite3
- Git
- Virtual environment (recommended)

## 📁 Project Structure

<pre lang="markdown">
fitness_api/
  ├──app/
            ├──__init__.py
          
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
    ├──create_tables.py
    ├──.gitignore
    ├──.env
    ├──README.md
</pre>

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sivaranjini005/fitness_api.git
cd fitness_api
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python create_tables.py
python seed_data.py
```

### 5. Run the Application
```bash
python run.py
```

Base URLs:
- API Base URL: http://127.0.0.1:8000
- Swagger Docs: http://127.0.0.1:8000/docs

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following configurations:

```env
DATABASE_URL=sqlite:///./fitness.db
DEBUG=True
LOG_LEVEL=INFO
PORT=8000
HOST=127.0.0.1
```

## 📚 API Documentation

### Available Endpoints

#### 1. List All Classes
`GET /classes/`

**Parameters:**
- `page` (optional): Page number for pagination
- `limit` (optional): Items per page

**Response:**
```json
{
  "classes": [
    {
      "id": 1,
      "name": "Yoga Basic",
      "instructor": "John Doe",
      "start_time": "2024-01-20T10:00:00Z",
      "available_slots": 10
    }
  ]
}
```

**Curl Example:**
```bash
curl -X GET "http://localhost:8000/classes/" -H "accept: application/json"
```

#### 2. Book a Class
`POST /bookings/book/`

**Request Body:**
```json
{
  "client_name": "User",
  "client_email": "user@gmail.com",
  "class_id": 1
}
```

**Response Codes:**
- 201: Booking created successfully
- 400: Invalid request
- 404: Class not found
- 422: Validation error

**Curl Example:**
```bash
curl -X POST "http://localhost:8000/bookings/book/" \
     -H "Content-Type: application/json" \
     -d '{"client_name": "User", "client_email": "user@gmail.com", "class_id": 1}'
```

## 🚨 Error Handling

Common error codes and their meanings:
- `400`: Invalid request parameters
- `404`: Resource not found
- `422`: Validation error (e.g., invalid email format, missing required fields)
- `429`: Too many requests (if rate limiting is enabled)
- `500`: Server error

## 🧪 Testing

Make sure the app is not running while running tests, since test cases create their own instance:

```bash
# Run all tests
pytest

# Run specific test files
pytest tests/test_classes.py
pytest tests/test_booking.py

# Run with coverage report
pytest --cov=app tests/
```

## 🚀 Deployment

### Production Deployment Steps

1. Server Setup:
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install required packages
   sudo apt install python3-pip python3-venv nginx
   ```

2. Configure Nginx:
   ```nginx
   server {
       listen 80;
       server_name your_domain.com;
       
       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

3. Set up SSL with Let's Encrypt
4. Configure environment variables for production
5. Set up database backups
6. Configure logging

## 📊 Monitoring and Logging

### Logging
- Application logs are stored in `app.log`
- Log rotation is configured to maintain log file size
- Different log levels: DEBUG, INFO, WARNING, ERROR

### Monitoring
- Health check endpoint: `/health`
- Metrics endpoint: `/metrics` (if implemented)
- Resource usage monitoring
- Error rate monitoring

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 guidelines
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 🔧 Troubleshooting

### Common Issues and Solutions

1. Database Connection Issues:
   - Check if SQLite file exists
   - Verify permissions on the database file
   - Ensure correct DATABASE_URL in .env

2. Import Errors:
   - Verify virtual environment is activated
   - Check if all dependencies are installed
   - Confirm Python version compatibility

3. Port Already in Use:
   - Check if another instance is running
   - Change port in .env file
   - Kill process using the port

## 📝 Changelog

### v1.0.0 (2024-01-01)
- Initial release
- Basic class booking functionality
- SQLite integration
- FastAPI implementation

### v1.1.0 (2024-01-15)
- Added pagination for class listing
- Improved error handling
- Added email validation
- Enhanced logging

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🧰 Technologies Used
- FastAPI    -- Supports asynchronous programming
- SQLAlchemy -- ORM
- SQLite     -- Database 
- Pydantic   -- Data validation
- Pytest     -- Unit Testing
- HTTPX      -- For async API testing

## 📬 Contact

For any questions, suggestions, or feedback, feel free to open an issue or reach out to the maintainers.

