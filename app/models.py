from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    password = Column(String)


class Course(Base):

    __tablename__ = "courses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String)

    description = Column(String)

    teacher = Column(String)


class Quiz(Base):

    __tablename__ = "quizzes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String)

    course_id = Column(
        Integer,
        ForeignKey("courses.id")
    )