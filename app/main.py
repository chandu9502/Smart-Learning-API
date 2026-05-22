from fastapi import FastAPI

from .database import engine
from .models import Base

from .routers import users
from .routers import courses
from .routers import quizzes


Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Smart Learning API"
)

app.include_router(users.router)

app.include_router(courses.router)

app.include_router(quizzes.router)


@app.get("/")
def home():

    return {
        "message": "Smart Learning API Running"
    }