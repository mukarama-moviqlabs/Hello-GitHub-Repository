
"""
This module checks whether a request contains
a valid API token before accessing protected endpoints.
"""

import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from config import API_TOKEN


# Tells FastAPI to look for a Bearer token in the request header.
security = HTTPBearer(auto_error=False)


def verify_api_token(
    credentials: HTTPAuthorizationCredentials | None = Depends(security)
):
    """
    Returns the token if valid.
    Rejects the request if the token is missing or incorrect.
    """

    # Check whether the user provided a token.
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Extract the actual token from the request.
    provided_token = credentials.credentials

    # Compare the provided token with stored secret.
    # compare_digest helps protect against timing-based comparison attacks.
    if not secrets.compare_digest(provided_token, API_TOKEN):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Allow the request to continue if authentication succeeds.
    return provided_token
