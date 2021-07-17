
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

	lapso_1: int
	lapso_2: int
	lapso_3: int

	result: int

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
	school_year:str

class RecordCreate(RecordBase):
	pass 

class Record(RecordBase):
	id: int
	student_id: int
	subjects: List[Subject] = []
	comments: List[Comment] = []