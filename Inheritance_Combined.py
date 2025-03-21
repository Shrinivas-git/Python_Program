class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

class Athlete(Person):
    def play_sport(self):
        print(f"{self.name} is playing sports")

class StudentAthlete(Student, Athlete):
    def manage_time(self):
        print(f"{self.name} balances studying and sports")

class Graduate(Person):
    def graduate(self):
        print(f"{self.name} has graduated")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

class WorkingStudent(Student, Person):
    def work(self):
        print(f"{self.name} is studying and working")

if __name__ == "__main__":
    # Single inheritance example
    print("Single inheritance")

    student_1 = Student("Alice")
    student_1.introduce()  # From Person
    student_1.study()      # From Student

    # Multiple inheritance example
    print("\nMultiple inheritance")

    student_athlete_1 = StudentAthlete("Bob")
    student_athlete_1.introduce()  # From Person
    student_athlete_1.study()      # From Student
    student_athlete_1.play_sport() # From Athlete
    student_athlete_1.manage_time()  # From StudentAthlete

    # Demonstrating inheritance with extra features
    print("\nGraduate example")

    graduate_1 = Graduate("Charlie")
    graduate_1.introduce()  # From Person
    graduate_1.graduate()   # From Graduate

    print("\nTeacher example")

    teacher_1 = Teacher("David")
    teacher_1.introduce()  # From Person
    teacher_1.teach()      # From Teacher

    # WorkingStudent example
    print("\nWorkingStudent example")

    working_student_1 = WorkingStudent("Eva")
    working_student_1.introduce()  # From Person
    working_student_1.study()      # From Student
    working_student_1.work()       # From WorkingStudent
