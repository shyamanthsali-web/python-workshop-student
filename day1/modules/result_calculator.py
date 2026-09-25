# TODO
# Create a function called calculate_percentage()

# It should :
# 1. Accept three marks
# 2. Calculate the total
# 3. Calculate the percentage
# 4. Return the percentage
def calculate_percentage(marks_sub1,marks_sub2,marks_sub3):
  total=(marks_sub1,marks_sub2,marks_sub3)
  percentage=(total/300)*100
  return percentage

def calculate_grade(percentage):
  grade=None
  if percentage>=80:
    grade="A"
  elif percentage>=60:
    grade="B"
  elif percentage>=40:
    grade="C"
  else:
    grade="D"

  return grade

if __name__