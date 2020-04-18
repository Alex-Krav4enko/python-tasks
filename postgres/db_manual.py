import psycopg2
from pprint import pprint
from typing import List

connect = psycopg2.connect(
    database='test_db',
    user='postgres',
    password='postgres'
)


class Student:
    def __init__(self, name: str, gpa: float, birth: str):
        self.name = name
        self.gpa = gpa
        self.birth = birth


def create_db():
    cur.execute("""create table if not exists student (
                id serial primary key,
                name character varying(100) not null,
                gpa numeric(10,2),
                birth timestamp with time zone);
                """)

    cur.execute("""create table if not exists course (
                id serial primary key,
                name character varying(100) not null);
                """)

    cur.execute("""create table if not exists student_course (
                id serial primary key,
                student_id integer not null references student(id),
                course_id integer not null references course(id));
                """)


def add_student(student: Student):
    cur.execute("""insert into student (name, gpa, birth) values (%s, %s, %s) returning id;""",
                (student.name, student.gpa, student.birth))
    return int(cur.fetchone()[0])


def add_students(students: List[Student], course_id: int):
    try:
        for i, student in enumerate(students):
            student_id = add_student(students[i])
            cur.execute("""insert into student_course (student_id, course_id) values (%s, %s);""",
                        (student_id, course_id))
    except psycopg2.DatabaseError as error:
        connect.rollback()
        pprint(error)


def get_student(student_id: int):
    cur.execute("""select * from student where id = %s;""",
                (student_id, ))
    return cur.fetchone()


def get_students(course_id: int):
    cur.execute("""select s.* from student_course sc 
                   join student s on s.id = sc.student_id
                   where sc.course_id = %s;""",
                (course_id, ))
    return cur.fetchall()


if __name__ == '__main__':
    alex = Student('Alex', 5.00, '1999-10-12')
    mike = Student('Mike', 4.25, '2000-08-04')
    kate = Student('Kate', 1.00, '1987-11-01')

    cur = connect.cursor()
    create_db()
    # add_students([alex, mike], 1)
    # add_students([kate], 3)
    # add_student(mike)
    # add_student(kate)
    # pprint(get_student(35))
    pprint(get_students(1))

    connect.commit()
    connect.close()
