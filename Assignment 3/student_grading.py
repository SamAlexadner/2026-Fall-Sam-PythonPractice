EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

exam_grade = 0
assignment_grade = 0
quiz_grade = 0

midterm_exam_grade = float(input("Please enter midterm exam grade 0 - 100: "))
final_exam_grade = float(input("Please enter final exam grade 0 - 100: "))
first_assignment_grade = float(input("Please enter first assignment grade 0 - 30: "))
second_assignment_grade = float(input("Please enter second assignment grade 0 - 30: "))
first_quiz_grade = float(input("Please enter firrt quiz grade 0 - 20: "))
second_quiz_grade = float(input("Please enter second quiz grade 0 - 20: "))

if (0 <= midterm_exam_grade <= 100) and (0 <= final_exam_grade <= 100):
    avg_exam_grade = (midterm_exam_grade + final_exam_grade) / 2  # calculate the average value
    exam_grade = (avg_exam_grade / 100) * EXAM_WEIGHT  # convert to a percentage ratio then time the Weight value
else:
    print("Invalid input. Please enter exams within the 0 - 100 range.")
if (0 <= first_assignment_grade <= 30) and (0 <= second_assignment_grade <= 30):
    avg_assignment_grade = (first_assignment_grade + second_assignment_grade) / 2
    assignment_grade  = (avg_assignment_grade / 30) * ASSIGNMENT_WEIGHT
else:
    print("Invalid input. Please enter assignments within the 0 - 30 range.")
if (0 <= first_quiz_grade <= 20) and (0 <= second_quiz_grade <= 20):
    avg_quiz_grade = (first_quiz_grade + second_quiz_grade) / 2
    quiz_grade = (avg_quiz_grade / 20) * QUIZ_WEIGHT
else:
    print("Invalid input. Please enter quizzes within the 0 - 20 range.")

# add the final ratio then back to the percentage ratio
final_grade_ratio = (exam_grade + assignment_grade + quiz_grade)  
print(f'The students final grade is {final_grade_ratio:.2%}')
