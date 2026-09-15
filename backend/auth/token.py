"""Authentication token module."""

def generate_token(username: str) -> str:
    return f"token-{username}"

# Added token refresh preparation
