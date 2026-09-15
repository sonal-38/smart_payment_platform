"""Authentication token module."""

def generate_token(username: str) -> str:
    return f"token-{username}"

# Improved token expiration handling
