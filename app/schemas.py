from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import field_validator

import re


class UserCreate(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str

    @field_validator("password")
    def validate_password(cls, value):

        if len(value) < 8:
            raise ValueError(
                "Password must be at least 8 characters"
            )

        if not re.search(r"[A-Z]", value):
            raise ValueError(
                "Password must contain uppercase letter"
            )

        return value


class UserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class CourseCreate(BaseModel):

    title: str = Field(
        min_length=5,
        max_length=100
    )

    description: str = Field(
        min_length=10,
        max_length=300
    )

    teacher: str


class CourseResponse(BaseModel):

    id: int
    title: str
    description: str
    teacher: str

    class Config:
        from_attributes = True


class QuizCreate(BaseModel):

    title: str = Field(
        min_length=3,
        max_length=100
    )

    course_id: int


class QuizResponse(BaseModel):

    id: int
    title: str
    course_id: int

    class Config:
        from_attributes = True