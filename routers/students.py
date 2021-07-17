
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
async def students(db: Session = Depends(get_db)):
    _students = db.query(models.Student).all()
    return {'data':_students}


@router.get('/all/name',response_model= Dict)
async def students(db: Session = Depends(get_db)):
    _students = db.query(models.Student).all()
    _students = [ student.first_name for student in _students]
    return {'data':_students}


@router.get('/detail',response_model= schemas.Student)
async def students(ci,db: Session = Depends(get_db)):
    _student = db.query(models.Student).filter(models.Student.ci == ci).first()
    return _student


@router.post('/create')
async def create_student(student: schemas.StudentEdit, db: Session = Depends(get_db)):
    _student = models.Student(**student.dict())
    db.add(_student)
    db.commit()
    return {'sucess': True}


@router.put('/edit')
async def edit_student(ci: str ,student: schemas.StudentEdit, db: Session = Depends(get_db)):
    _student = db.query(models.Student).filter(models.Student.ci == ci).first()
    #_student.__dict__.update(**student.dict()) odio sqlacchemy
    _student.first_name = student.first_name
    _student.last_name = student.last_name
    _student.email = _student.email
    _student.school_year = _student.school_year

    return {'success':_student.first_name}


@router.delete('/delete')
async def delete_student(ci: str, db: Session = Depends(get_db)):
    _student = db.query(models.Student).filter(models.Student.ci == ci).first()
    db.delete(_student)
    db.commit()
    return {'delete':True}


