from fastapi import APIRouter
from fastapi import Depends
from ..auth import hash_password
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..auth import verify_password
from ..auth import create_access_token
from ..database import SessionLocal
from .. import models
from .. import schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=schemas.UserResponse
)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):

    users = db.query(
        models.User
    ).all()

    return users

@router.post("/login")
def login(
    user: schemas.LoginRequest,
    db: Session = Depends(get_db)
):

    db_user = db.query(
        models.User
    ).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }