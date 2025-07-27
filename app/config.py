from dotenv import load_dotenv
import os

load_dotenv()

CORS_ORIGINS = os.getenv("CORS_ORIGINS_ALLOWED")
CORS_ORIGINS = [origin.strip() for origin in CORS_ORIGINS.split(",") if origin]

CORS_CREDENTIAL = os.getenv("CORS_CREDENTIAL")

CORS_METHODS_ALLOWED = os.getenv("CORS_METHODS_ALLOWED")
CORS_METHODS_ALLOWED = [method.strip() for method in CORS_METHODS_ALLOWED.split(",") if method]

CORS_HEADERS_ALLOWED = os.getenv("CORS_HEADERS_ALLOWED")
CORS_HEADERS_ALLOWED = [header.strip() for header in CORS_HEADERS_ALLOWED.split(",") if header]

DOMAIN = os.getenv("DOMAIN")