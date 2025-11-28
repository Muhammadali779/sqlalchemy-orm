from datetime import datetime
from sqlalchemy import(
    Column, String, Boolean, Float, Integer, Date, DateTime, Text, ForeignKey
)
from sqlalchemy.orm import relationship
from .db import Base, get_db



class Student(Base):
    __tablename__ = 'students'

    student_id = Column('student_id', Integer, primary_key=True, nullable=False)
    first_name = Column('first_name', String(length=64), nullable=False)
    last_name = Column('last_name', String(length=64), nullable=False)
    birthdate = Column('birthdate', DateTime, nullable=False)
    gender = Column('gender', String(length=20), nullable= False)
    bio = Column ('bio', String(length=256))
    gpa = Column('gpa', Float, nullable=False)

    
    certificates = relationship('Certificate', back_populates='student')

    def __str__(self):
        return f'Student (id= {self.student_id}, Name= ( {self.first_name} {self.last_name}))'
    
    def __repr__(self):
        return f'Student (id= {self.student_id}, Name= ( {self.first_name} {self.last_name}))'
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

class Certificate(Base):
    __tablename__ = 'certificates'
    id = Column('id', Integer, primary_key=True, nullable=False)
    student_id = Column('student_id', ForeignKey('students.student_id', ondelete='CASCADE'))
    title = Column('title', String(length=256), nullable=False)
    content = Column('content', Text, nullable=False)
    issued_at = Column('issued_at', DateTime, default=datetime.now)
    certificate_code = Column('certificate_code', String(256), unique=True)
    is_verified = Column('is_verified', Boolean, default=False)

    student = relationship('Student', back_populates='certificates')


    def __str__(self):
        return f"Certificate(title={self.title}, code={self.certificate_code}, student_id={self.student_id})"

    
    def __repr__(self):
        return f"<Certificate id={self.id}, title='{self.title}', student_id={self.student_id}>"
