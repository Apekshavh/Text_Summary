from typing import List, Dict

class Config:
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",  # React dev server
        "http://127.0.0.1:5173"   # Alternative local dev URL
    ]
    
    CORS_CONFIG: Dict = {
        r"/api/*": {
            "origins": CORS_ORIGINS,
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "expose_headers": ["Content-Range", "X-Content-Range"],
            "supports_credentials": True,
            "max_age": 600  # Cache preflight requests for 10 minutes
        }
    }