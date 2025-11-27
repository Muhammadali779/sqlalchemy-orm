from datetime import date
from school.create_tables import init_db
from school.crud import (
    create_student,
    get_students,
    get_one_student_by_id,
    update_student,

)

init_db()


# create_student('ali', 'valiyev3', date(2005, 9, 3), 'male', 'matematik', 4.5)

# students = get_students()
# print(students)


# one_student = get_one_student_by_id(2)
# print(one_student.first_name, one_student.gpa)

# update = update_student(2, gpa= 2.22)

