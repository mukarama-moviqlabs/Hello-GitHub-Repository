
"""
secure_api.py

A protected API endpoint built using FastAPI.

The endpoint requires valid API-token authentication
before allowing access.
"""

from fastapi import FastAPI, Depends

# Import our authentication function.
from auth import verify_api_token

# Create the FastAPI application.
app = FastAPI(
    title="Secure Eligibility API",
    description="A practice API with token-based authentication",
    version="1.0.0"
)


# Create a protected endpoint.
@app.get("/api/v1/protected")
def protected_endpoint(
    token: str = Depends(verify_api_token)
):
    """
    This endpoint can only be accessed with a valid API token.
    """

    # Return a success response after authentication.
    return {
        "authenticated": True,
        "message": "Access granted. Authentication successful."
    }
