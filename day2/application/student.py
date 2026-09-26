class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        total = self.python + self.mathematics + self.communication

        return total / 3

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.grade())

    def grade(self):
        """Determine the student's grade based on percentage."""
        percentage = self.calculate_percentage()
        if percentage >= 80:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 40:
            return "C"
        else:
            return "D"

if __name__ =="__main__":
                obj_1 = Student("rohit",20,40,54,65)
                obj_2 = Student("raj",34,54,66,72)
                obj_3 = Student("gowda",77,76,87,56)
                obj_1.display()
                obj_2.display()
                obj_3.display()