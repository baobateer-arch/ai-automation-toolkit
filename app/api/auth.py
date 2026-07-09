from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database import async_session
from app.models.user import User
from app.services.auth_service import hash_password, verify_password
from app.services.jwt_service import create_access_token

router = APIRouter()


class _RegisterRequest(BaseModel):
    email: str
    password: str


class _LoginRequest(BaseModel):
    email: str
    password: str


class _AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/api/auth/register", response_model=_AuthResponse)
async def register(body: _RegisterRequest):
    if not body.email or not body.password:
        raise HTTPException(status_code=422, detail="Email and password are required")
    if len(body.password) < 6:
        raise HTTPException(status_code=422, detail="Password must be at least 6 characters")

    async with async_session() as session:
        from sqlalchemy import select
        existing = (await session.execute(
            select(User).where(User.email == body.email)
        )).scalar_one_or_none()
        if existing:
            raise HTTPException(status_code=409, detail="Email already registered")

        user = User(
            email=body.email,
            password_hash=hash_password(body.password),
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

    token = create_access_token({"sub": str(user.id), "email": user.email})
    return _AuthResponse(access_token=token)


@router.post("/api/auth/login", response_model=_AuthResponse)
async def login(body: _LoginRequest):
    if not body.email or not body.password:
        raise HTTPException(status_code=422, detail="Email and password are required")

    async with async_session() as session:
        from sqlalchemy import select
        user = (await session.execute(
            select(User).where(User.email == body.email)
        )).scalar_one_or_none()
        if not user or not verify_password(body.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(user.id), "email": user.email})
    return _AuthResponse(access_token=token)
