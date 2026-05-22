from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

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
        password=user.password
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