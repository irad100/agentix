import httpx
import jwt
from langgraph import Auth, exceptions
import os
CLERK_JWKS_URL = "https://api.clerk.dev/jwks"
_jwks_cache = None

async def _get_jwks() -> dict:
    global _jwks_cache
    if _jwks_cache is None:
        resp = httpx.get(CLERK_JWKS_URL)
        resp.raise_for_status()
        _jwks_cache = resp.json()
    return _jwks_cache

@Auth.authenticate
async def auth(authorization: str | None) -> Auth.types.MinimalUserDict:
    """
    Validate Clerk JWT from the Authorization header
    and return a minimal user dict for LangGraph.
    """
    if not authorization:
        raise exceptions.HTTPException(status_code=401, detail="Missing Authorization header")
    try:
        scheme, token = authorization.split()
    except ValueError:
        raise exceptions.HTTPException(status_code=401, detail="Invalid Authorization header format")
    if scheme.lower() != "bearer":
        raise exceptions.HTTPException(status_code=401, detail="Unsupported auth scheme")

    jwks = await _get_jwks()
    try:
        # Audience should match Clerk’s Frontend API audience or your API identifier
        payload = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            audience=os.getenv("CLERK_PUBLISHABLE_KEY")  # e.g. your Clerk API key or custom identifier
        )
    except jwt.PyJWTError:
        raise exceptions.HTTPException(status_code=401, detail="Invalid or expired token")

    # Return the user identity to LangGraph
    return {
        "identity": payload["sub"],    # Clerk user ID
        "claims": payload             # optional: include full claims if you need them
    }