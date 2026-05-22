from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post(
    "/",
    response_model=schemas.CourseResponse
)
def create_course(
    course: schemas.CourseCreate,
    db: Session = Depends(get_db)
):

    new_course = models.Course(
        title=course.title,
        description=course.description,
        teacher=course.teacher
    )

    db.add(new_course)

    db.commit()

    db.refresh(new_course)

    return new_course


@router.get("/")
def get_courses(
    db: Session = Depends(get_db)
):

    courses = db.query(
        models.Course
    ).all()

    return courses