from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.database.schema.user_schema import UserSchema
from app.helper import hashPassword, verifyPassword, createAccessToken
from app.models.auth import Register, Login


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(data: Login, db: Annotated[Session, Depends(get_db)]):
    user = db.query(UserSchema).filter(UserSchema.email == data.email).first()

    if not user or not verifyPassword(data.password, user.password):
        return JSONResponse(
            content={"message": "Invalid email or password"},
            status_code=401,
        )

    payload={
        "id":user.id,
        "name":user.name,
        "email":user.email
    }

    token=createAccessToken(payload)
    payload["access_token"] ="Bearer " + token

    return {"message": "Login successful", "data":payload}

@router.post("/register")
def register(
    data: Register,
    db: Annotated[Session, Depends(get_db)]
):
    existing_user = (
        db.query(UserSchema)
        .filter(UserSchema.email == data.email)
        .first()
    )

    if existing_user:
        return JSONResponse(
            content={
                "message": "User with this email already exists"
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    new_user = UserSchema(
        name=data.name,
        email=data.email,
        password=hashPassword(data.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "is_active": new_user.is_active,
            "created_at": new_user.created_at,
            "updated_at": new_user.updated_at,
        },
    }