"""This module contains the authentication logic for the application.

It is used to authenticate the user and get the user's claims.
"""

import asyncio
import logging
import os

import httpx
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions
from langgraph_sdk import Auth

auth = Auth()

logger = logging.getLogger(__name__)


@auth.authenticate
async def authenticate(request: httpx.Request) -> Auth.types.MinimalUserDict:
    """Authenticate the user and return the user's claims."""
    sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))
    request_state = await asyncio.to_thread(
        sdk.authenticate_request,
        request,
        AuthenticateRequestOptions(),
    )

    if not request_state.is_signed_in or not request_state.payload:
        raise Auth.exceptions.HTTPException(
            status_code=401,
            detail=f"Unauthorized: {request_state.reason}",
        )

    return {
        "identity": request_state.payload.get("sub", ""),
    }
