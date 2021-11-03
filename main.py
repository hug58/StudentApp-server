
from routers import handlers
from fastapi import FastAPI
from routers.handlers import api_router
import uvicorn
#locals
from app_database.database import engine
from app_database import models


'''JWT
    SECURITY
'''


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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