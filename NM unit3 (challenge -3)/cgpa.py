class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students_list):
    sorted_students = sorted(students_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

student1 = Student("jeny", "B123", 3.7)
student2 = Student("aani", "B125", 3.9)
student3 = Student("faran", "B126", 3.5)
student4 = Student("charles", "B124", 3.8)

students = [student1, student2, student3, student4]
sorted_students = sort_students(students)

for student in sorted_students:
    print(f"name: {student.name}, roll number: {student.roll_number}, cgpa: {student.cgpa}")
