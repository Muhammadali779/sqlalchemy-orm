from datetime import datetime
from sqlalchemy import(
    Column, String, Boolean, Float, Integer, Date, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from .db import Base



class Student(Base):
    __tablename__ = 'students'

    student_id = Column('student_id', Integer, primary_key=True, nullable=False)
    first_name = Column('first_name', String(length=64), nullable=False)
    last_name = Column('last_name', String(length=64), nullable=False)
    birthdate = Column('birthdate', DateTime, nullable=False)
    gender = Column('gender', String(length=20), nullable= False)
    bio = Column ('bio', String(length=256))
    gpa = Column('gpa', Float, nullable=False)


    def __str__(self):
        return f'Student (id= {self.student_id}, Name= ( {self.first_name} {self.last_name}))'
    
    def __repr__(self):
        return f'Student (id= {self.student_id}, Name= ( {self.first_name} {self.last_name}))'
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

