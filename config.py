
"""
config.py

Central configuration module for the Secure Eligibility API.

This module loads environment variables and makes application
configuration available to other Python files.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Get the absolute path of the directory containing this file.
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from the .env file.
load_dotenv(BASE_DIR / ".env")

# Read the API authentication token from the environment.
API_TOKEN = os.getenv("API_TOKEN")

# Read the application environment.
# Use development as the default if APP_ENV is not configured.
APP_ENV = os.getenv("APP_ENV", "development")

# Stop application configuration if the required API token is missing.
if not API_TOKEN:
    raise RuntimeError("API_TOKEN is missing. Check your .env file.")
