from dotenv import (
    load_dotenv,
)  # loading .env file to get the environment variables before application startup

load_dotenv()

from app.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
