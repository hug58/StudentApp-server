
from typing import List, Optional
from pydantic import BaseModel



"""
Estudiantes
"""

class StudentBase(BaseModel):
	
	first_name: str
	last_name: str
	ci:str


	email: str
	is_active: bool


class StudentEdit(StudentBase):

	hashed_password: str

	class Config:
		orm_mode = True


class Student(StudentBase):

	id: int
	
	class Config:
		orm_mode = True


"""
Notas
"""

class SubjectBase(BaseModel):
	title:str
	notes: List


class SubjectCreate(SubjectBase):   
	pass

class Subject(SubjectBase):
	id: int
	record_id: int

	class Config:
		orm_mode = True

"""
COMENTARIOS
"""

class CommentBase(BaseModel):
	text:str

class CommentCreate(BaseModel):
	pass

class Comment(CommentBase):
	id: int
	record_id: int

	class Config:
		orm_mode = True



"""
HISTORIAL
"""


class RecordBase(BaseModel):
	school_year:int
	student_id:int
	section:str

class RecordCreate(RecordBase):
	subjects: List[SubjectCreate] 

class Record(RecordBase):
	id: int
	subjects: List[Subject]
	comments: List[Comment] 


"""
Notas
"""

class SubjectBaseTable(BaseModel):
	title:str

class SubjectCreateTable(SubjectBase):   
	pass

class Subject(SubjectBase):
	id: int
	record_id: int

	class Config:
		orm_mode = True


"""
HISTORIAL TABLE
"""
class RecordBaseTable(BaseModel):
	school_year:int

class RecordCreateTable(RecordBaseTable):
	titles: List[str] 

class RecordTable(RecordBaseTable):
	id: int
	titles: List[str] 
	created_at: str
