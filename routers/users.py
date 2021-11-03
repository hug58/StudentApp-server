from fastapi import APIRouter, Depends
from typing import List,Dict

import sys
sys.path.append('..')

from sqlalchemy.orm import Session
from app_database.database import get_db

from app_database import schemas
from app_database import models


router = APIRouter()


@router.get('/all',response_model= Dict)
async def records_all(student_id:int,db: Session = Depends(get_db)):
    _records = db.query(models.Record).filter(models.Record.student_id==student_id).all()
    return {'data':_records}



@router.post('/create')
async def create_record(record: schemas.RecordCreateTable, db: Session = Depends(get_db)):
	data = record.dict()
	_record = models.HistorialTable(**data)
	db.add(_record)
	db.commit()
	return {'sucess': True}