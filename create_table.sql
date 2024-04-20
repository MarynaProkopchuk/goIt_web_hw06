--Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY,
    name VARCHAR (150) NOT NULL
 );

 --Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    fullname VARCHAR (150) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
        on delete cascade
 );

  --Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    fullname VARCHAR (150) NOT NULL);

--Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name VARCHAR (150) NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        on delete cascade
 );

--Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    grade_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
        on delete cascade,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
        on delete cascade
 );