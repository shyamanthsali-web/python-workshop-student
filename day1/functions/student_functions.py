# Day 1 - Python Fundamentals
def input_student():
    student_name = input("Enter student name:")
    marks_python = float(input("Enter marks for Python:"))
    marks_math = float(input("Enter marks for Mathematics:"))
    marks_comm = float(input("Enter marks for Communication:"))
    dict_student_info = {
        "name": student_name,
        "python": marks_python,
        "math": marks_math,
        "comm": marks_comm
    }
    return dict_student_info
   # return student_name,marks_comm,marks_python,marks_math


# TODO:
def calculate_percentage(marks_python, marks_math, marks_comm):
    total = (marks_comm+marks_math+marks_python)
    percentage = (total/3)*100
    return percentage


if __name__ == "__main__":
    print("\n -- Result --")
    student_info = input_student()
    print(student_info)
    print("Student:", student_info["name"])
    print("Percentage", calculate_percentage(student_info["python"],
                                             student_info["math"],
                                             student_info["comm"])
          )
