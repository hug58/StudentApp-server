from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import ARRAY
from .database import Base


class User(Base):
    __abstract__= True
    #__tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)

    email = Column(String, unique=True, index=True)
    type_in = Column(String)

    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)




class Student(User):
    __tablename__ = "students"

    ci = Column(String(10),unique=True)
    records = relationship("Record", back_populates="student")

class Record(Base):
    __tablename__ = "records"

    school_year = Column(Integer, index=True)
    section = Column(String(10))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    id = Column(Integer, primary_key=True, index=True)

    #Sql alchemy aveces es confuso, pero tienes que relacionarlos to a to
    #el estudiante malo
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="records")
    
    #comentarios
    comment = relationship("Comment", back_populates="record")
    
    #notas
    subjects = relationship("Subjects", back_populates="record")



class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)

    text = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    record_id = Column(Integer, ForeignKey("records.id"))
    record = relationship("Record", back_populates="comment")


class Subjects(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)

    record_id = Column(Integer, ForeignKey("records.id"))
    record = relationship("Record", back_populates="subjects")

    title = Column(String, index=True)
    notes = Column(ARRAY(Integer()))



    
class HistorialTable(Base):
    __tablename__ = "historial_tables"
    id = Column(Integer, primary_key=True, index=True)

    school_year = Column(Integer, index=True)
    titles = Column(ARRAY(String(100)))
