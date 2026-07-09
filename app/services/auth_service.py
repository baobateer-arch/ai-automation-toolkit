import hashlib
import secrets


def hash_password(password: str) -> str:
    """
    Hash a password using PBKDF2-SHA256 with a random 16-byte salt.
    Returns a string in the format ``salt$hash`` (both hex-encoded).
    """
    salt = secrets.token_hex(16)
    pwd_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100000,
    )
    return f"{salt}${pwd_hash.hex()}"


def verify_password(password: str, stored: str) -> bool:
    """
    Verify a plain-text password against a ``salt$hash`` string
    produced by :func:`hash_password`.
    """
    try:
        salt, pwd_hash = stored.split("$", 1)
    except ValueError:
        return False
    computed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100000,
    )
    return computed.hex() == pwd_hash
