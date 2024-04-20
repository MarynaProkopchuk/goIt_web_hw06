from datetime import datetime
import random
import sqlite3
from faker import Faker

NUMBER_STUDENTS = 10
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 2

fake_data =Faker()

with sqlite3.connect('db_table.db') as con:
    cur = con.cursor()


    for _ in range(NUMBER_GROUPS):
        cur.execute("INSERT INTO groups (name) VALUES (?)", (fake_data.license_plate(), ))

    for group_id in range(1, NUMBER_GROUPS+1):
        for _ in range(NUMBER_STUDENTS):
            cur.execute("INSERT INTO students (fullname, group_id) VALUES (?, ?)", (fake_data.name(), group_id))

    for _ in range(NUMBER_TEACHERS):
        cur.execute("INSERT INTO teachers (fullname) VALUES (?)", (fake_data.name(),))

    for teacher_id in range(1, NUMBER_TEACHERS+1):
        for _ in range(NUMBER_SUBJECTS):
            cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (fake_data.job(), teacher_id))

    for student_id in range(1, NUMBER_STUDENTS+1):
        for subject_id in range(1, (NUMBER_SUBJECTS*NUMBER_TEACHERS)+1):
            for _ in range(NUMBER_TEACHERS):
                        cur.execute(
                            "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
                            (student_id, subject_id, random.randint(0, 100), fake_data.date_between_dates(date_start=datetime(2023,9,1), date_end=datetime.today())))


try:
    # Збереження змін
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
finally:
    # Закриття підключення
    cur.close()
    con.close()













