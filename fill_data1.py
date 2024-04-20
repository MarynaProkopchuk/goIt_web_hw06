from datetime import datetime
import random
import sqlite3
from faker import Faker

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 4
NUMBER_SUBJECTS = 5
NUMBER_GRADES = 20

fake_data =Faker()

def generate_data(number_groups, number_students, number_teachers, number_subjects, number_grades):
    fake_students =[]
    fake_groups = []
    fake_teachers = []
    fake_subjects = []
    fake_grades = []

    for _ in range(number_groups):
        fake_groups.append(fake_data.license_plate())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_grades*number_students):
        fake_grades.append(fake_data.date_between_dates(date_start=datetime(2023,9,1), date_end=datetime.today()))

    return fake_groups, fake_students, fake_teachers, fake_subjects, fake_grades

def preaper_data(groups, students, teachers, subjects, grades):
    for_groups = []
    for_students = []
    for_teachers = []
    for_subjects = []
    for_grades = []
    for group in groups:
        for_groups.append((group, ))

    for student in students:
        for_students.append((student, random.randint(1, NUMBER_GROUPS)))

    for teacher in teachers:
        for_teachers.append((teacher, ))

    for subject in subjects:
        for_subjects.append((subject, random.randint(1, NUMBER_TEACHERS)))

    for grade in grades:
        for_grades.append((random.randint(1, NUMBER_STUDENTS), random.randint(1, NUMBER_SUBJECTS), random.randint(0, 100), grade))

    return for_groups, for_students,for_teachers, for_subjects, for_grades

def insert_data_to_db(groups, students, teachers, subjects, grades):
    with sqlite3.connect('db_table.db') as con:
        cur = con.cursor()
        sql_to_groups = """INSERT INTO groups(name) VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(fullname, group_id) VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(fullname) VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(name, teacher_id) VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_grades = """INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        con.commit()

if __name__ == '__main__':
    groups, students, teachers, subjects, grades = preaper_data(*generate_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_SUBJECTS, NUMBER_GRADES))
    insert_data_to_db(groups, students, teachers, subjects, grades)

