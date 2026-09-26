# TODO
# Create a function called calculate_percentage()

# It should :
# 1. Accept three marks
# 2. Calculate the total
# 3. Calculate the percentage
# 4. Return the percentage

def calculate_percentage(marks_1, marks_2, marks_3):
    total = (marks_1+marks_2+marks_3)
    percentage = (total/3)*100
    return percentage


def calculate_grade(percentage):
    grade = None
    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "D"
    return grade


if __name__ == "__main__":
    percentage = calculate_percentage(23, 34, 45)
    grade = calculate_grade(percentage=percentage)
