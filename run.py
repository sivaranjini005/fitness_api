"""
Entry point to run the FastAPI application using Uvicorn.
Loads environment variables from .env before startup.
"""

from dotenv import load_dotenv

# Load .env variables early so they are available for all imports
load_dotenv()

from app.main import app
import uvicorn
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting app on http://{host}:{port}")

    uvicorn.run("app.main:app", host=host, port=port, reload=True)
