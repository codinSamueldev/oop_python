
class Student:

    def __init__(self, name: str, age: int, year: int):
        self.name = name
        self.age = age
        self.year = year


    def study(self):
        study = input(f"\nWhat subject {self.name} is studying? -> ").capitalize()
        
        return study


def get_student_name(times):
    name = input(f"\nType student {times + 1} name: ").capitalize()
    return name


def get_student_age():
    age = int(input("Type student's age: "))
    return age


def get_student_year():
    year = int(input("Type your current high-school year: "))
    return year


if __name__ == "__main__":
    teacher_input = int(input("Teacher, type how many students you want to add in the database: "))
    
    # Create a list of students using list comprehension.
    students_list = [Student(get_student_name(_), get_student_age(), get_student_year()) for _ in range(teacher_input)]
    students_db = []

    # Append important student information.
    for student in students_list:
        subject = student.study()
        students_db.append([student.name, student.age, subject])

    print(f"""
          STUDENT DATABASE
          {students_db}
          """)
