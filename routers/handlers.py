from fastapi import APIRouter

from routers import students

api_router = APIRouter()
api_router.include_router(students.router,prefix='/students',tags=['students'])