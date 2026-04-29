
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grades(self, grade):
        """
        Add a grade to the list of grades for the student.
        """
        self.grades.append(grade)

    def calculate_average(self):
        """
        Calculate the average of all grades.
        """
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_student_info(self):
        """
        Display student information.
        """
        average = self.calculate_average()
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)
        print("Average Grade:", average)


# Example usage
student1 = Student("Sudha Balam", 21)

student1.add_grades(90)
student1.add_grades(85)
student1.add_grades(92)

student1.display_student_info()