"""Auth module for Clerk JWT authentication."""

import os
from typing import Any, Optional, cast

import httpx
import jwt
from langgraph_sdk import Auth

CLERK_JWKS_URL = "https://api.clerk.dev/jwks"
_jwks_cache: Optional[dict[str, Any]] = None


async def _get_jwks() -> dict[str, Any]:
    global _jwks_cache
    if _jwks_cache is None:
        resp = httpx.get(CLERK_JWKS_URL)
        resp.raise_for_status()
        _jwks_cache = cast(dict[str, Any], resp.json())
    return _jwks_cache


auth = Auth()


@auth.authenticate
async def authenticate(authorization: str | None) -> Auth.types.MinimalUserDict:
    """Validate Clerk JWT from the Authorization header.

    Args:
        authorization: The Authorization header value.

    Returns:
        A minimal user dict for LangGraph.
    """
    if not authorization:
        raise Auth.exceptions.HTTPException(
            status_code=401, detail="Missing Authorization header"
        )
    try:
        scheme, token = authorization.split()
    except ValueError:
        raise Auth.exceptions.HTTPException(
            status_code=401, detail="Invalid Authorization header format"
        )
    if scheme.lower() != "bearer":
        raise Auth.exceptions.HTTPException(
            status_code=401, detail="Unsupported auth scheme"
        )

    jwks = await _get_jwks()
    try:
        # Audience should match Clerk's Frontend API audience or your API identifier
        key = ""
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")

        if not kid:
            raise Auth.exceptions.HTTPException(
                status_code=401, detail="Token missing kid header"
            )

        key_found = False
        for jwk in jwks.get("keys", []):
            if jwk.get("kid") == kid:
                key = jwt.PyJWK(jwk).key
                key_found = True
                break

        if not key_found:
            global _jwks_cache
            _jwks_cache = None
            refreshed_jwks = await _get_jwks()
            for jwk in refreshed_jwks.get("keys", []):
                if jwk.get("kid") == kid:
                    key = jwt.PyJWK(jwk).key
                    key_found = True
                    break
            if not key_found:
                raise Auth.exceptions.HTTPException(
                    status_code=401, detail="Public key not found in JWKS"
                )

        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=os.getenv(
                "CLERK_PUBLISHABLE_KEY"
            ),  # e.g. your Clerk API key or custom identifier
        )
    except jwt.PyJWTError as e:
        raise Auth.exceptions.HTTPException(
            status_code=401, detail=f"Invalid or expired token: {e}"
        )

    # Return the user identity to LangGraph
    return {
        "identity": payload["sub"],  # Clerk user ID
    }
