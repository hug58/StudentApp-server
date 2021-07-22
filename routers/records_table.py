
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
async def records_all(db: Session = Depends(get_db)):
    _records = db.query(models.HistorialTable).all()
    return {'data':_records}

@router.get('/detail',response_model= Dict)
async def records_all(id:int,db: Session = Depends(get_db)):
    _records = db.query(models.HistorialTable).get(id)
    return {'data':_records}



@router.post('/create')
async def create_record(record: schemas.RecordCreateTable, db: Session = Depends(get_db)):
	data = record.dict()
	_record = models.HistorialTable(**data)
	db.add(_record)
	db.commit()
	return {'sucess': True}





@router.delete('/delete')
async def delete_student(id: str, db: Session = Depends(get_db)):
    _record = db.query(models.HistorialTable).get(id)
    db.delete(_record)
    db.commit()

    return {'delete':True}