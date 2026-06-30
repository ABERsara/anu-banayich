"""
Authentication service.

Handles registration, OTP, login, JWT issuance.

TODO list for junior developer:
  [ ] implement register() – create user, hash password, send OTP
  [ ] implement verify_otp() – compare code, mark pending_approval
  [ ] implement login() – verify password, issue JWT pair
  [ ] implement refresh_token() – validate refresh JWT, issue new access token
"""

import random
import string
from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.constants import AccountStatus, UserRole
from app.core.security import ALGORITHM, get_password_hash, verify_password
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.services.email_service import send_otp_email


def _generate_otp(length: int = 6) -> str:
    return "".join(random.choices(string.digits, k=length))


def _create_token(subject: str, expires_delta: timedelta, token_type: str = "access") -> str:
    expire = datetime.now(UTC) + expires_delta
    payload = {"sub": subject, "exp": expire, "type": token_type}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)


def register(db: Session, data: RegisterRequest) -> User:
    """
    Step 1: Create a new user account and send OTP.

    TODO:
      1. Check if email already exists → raise 400
      2. Hash the password with get_password_hash()
      3. Create the User object and save to DB
      4. Generate OTP, save it + expiry on the user, send email
      5. Return the created user
    """
    # TODO: implement this function
    raise NotImplementedError("register() is not yet implemented")


def verify_otp(db: Session, email: str, otp_code: str) -> User:
    """
    Step 2: Verify OTP and move user to pending_approval status.

    TODO:
      1. Find user by email
      2. Check OTP code matches and hasn't expired
      3. Update status to PENDING_APPROVAL
      4. Clear the OTP from the DB
      5. Return the user
    """
    # TODO: implement this function
    raise NotImplementedError("verify_otp() is not yet implemented")


def login(db: Session, data: LoginRequest) -> TokenResponse:
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="אימות נכשל. בדקי מייל וסיסמה.")
    if user.account_status != AccountStatus.ACTIVE:
        raise HTTPException(status_code=403, detail="החשבון אינו פעיל. פנה/י למנהל.")
    access = _create_token(user.id, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES), "access")
    refresh = _create_token(user.id, timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS), "refresh")
    return TokenResponse(access_token=access, refresh_token=refresh, token_type="bearer")


def refresh_token(db: Session, refresh_tok: str) -> TokenResponse:
    try:
        payload = jwt.decode(refresh_tok, settings.SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="טוקן רענון לא תקין.")
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="טוקן רענון לא תקין.")
    user_id: str | None = payload.get("sub")
    user = db.query(User).filter(User.id == user_id).first()
    if not user or user.account_status != AccountStatus.ACTIVE:
        raise HTTPException(status_code=401, detail="טוקן רענון לא תקין.")
    access = _create_token(user.id, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES), "access")
    return TokenResponse(access_token=access, refresh_token=refresh_tok, token_type="bearer")


def resend_otp(db: Session, email: str) -> None:
    """
    Resend OTP to a user still in PENDING_OTP status.

    TODO:
      1. Find user by email
      2. Verify status is PENDING_OTP
      3. Generate new OTP, update expiry
      4. Send email
    """
    # TODO: implement this function
    raise NotImplementedError("resend_otp() is not yet implemented")
