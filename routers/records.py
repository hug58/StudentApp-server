
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




@router.get('/detail',response_model= Dict)
async def records_detail(record_id:int,db: Session = Depends(get_db)):
    _records = db.query(models.Record).get(record_id)
    _subjects =  db.query(models.Subjects).filter(models.Subjects.record_id==record_id).all()
    return {'data':{'record':_records,'subjects':_subjects}}




@router.post('/create')
async def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db)):
	data = record.dict()
	subjects = data.pop('subjects')

	_record = models.Record(**data)
	
	db.add(_record)
	db.commit()


	for subject in subjects:
		_subject = models.Subjects(record_id=_record.id,**subject)
		db.add(_subject)
		db.commit()


	return {'sucess': True}




@router.delete('/delete')
async def delete_record(id: int, db: Session = Depends(get_db)):
    _record= db.query(models.Record).get(models.id == id)
    db.delete(_student)
    db.commit()
    return {'delete':True}


