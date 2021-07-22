from fastapi import APIRouter

from routers import students
from routers import records
from routers import records_table


api_router = APIRouter()
api_router.include_router(students.router,prefix='/students',tags=['students'])
api_router.include_router(records.router,prefix='/students/records',tags=['records_students'])
api_router.include_router(records_table.router,prefix='/records',tags=['records'])
