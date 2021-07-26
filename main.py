
from routers import handlers
from fastapi import FastAPI
from routers.handlers import api_router
import uvicorn
#locals
from app_database.database import engine
from app_database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def home():
    return {"Hello": "FastAPI"}



@app.on_event("startup")
async def startup():
    # create db tables
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    #Base.metadata.drop_all()
    #Base.metadata.create_all()
    
if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')