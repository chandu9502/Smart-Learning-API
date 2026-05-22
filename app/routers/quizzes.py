from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"]
)


@router.post(
    "/",
    response_model=schemas.QuizResponse
)
def create_quiz(
    quiz: schemas.QuizCreate,
    db: Session = Depends(get_db)
):

    new_quiz = models.Quiz(
        title=quiz.title,
        course_id=quiz.course_id
    )

    db.add(new_quiz)

    db.commit()

    db.refresh(new_quiz)

    return new_quiz


@router.get("/")
def get_quizzes(
    db: Session = Depends(get_db)
):

    quizzes = db.query(
        models.Quiz
    ).all()

    return quizzes