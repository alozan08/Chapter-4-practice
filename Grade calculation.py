''' Calculates the overall grade for four equally
    weighted programming assignments
    where each assignment is graded out of 50 points.
'''
# programming_score1 = float(input("Enter your score1: "))
# programming_score2 = float(input("Enter your score2: "))
# programming_score3 = float(input("Enter your score3: "))
# programming_score4 = float(input("Enter your score4: "))
#
# programming_percent1 = (score1/50) *100
# programming_percent2 = (score2/50) *100
# programming_percent3 = (score3/50) *100
# programming_percent4 = (score4/50) *100
#
# overall_grade = (programming_percent1 + programming_percent2 + programming_percent3 + programming_percent4)/4
# print("Your final score is:", overall_grade, '%')

''' Calculates the overall grade for four equally weighted 
    programming assignments, where assignments 1 and 2 are 
    graded out of 50 points and assignments 3 and 4 are 
    graded out of 75 points.
'''
# programming_score1 = float(input("Enter your score1: "))
# programming_score2 = float(input("Enter your score2: "))
# programming_score3 = float(input("Enter your score3: "))
# programming_score4 = float(input("Enter your score4: "))
#
# programming_percent1 = (score1/50) *100
# programming_percent2 = (score2/50) *100
# programming_percent3 = (score3/75) *100
# programming_percent4 = (score4/75) *100
#
# overall_grade = (programming_percent1 + programming_percent2 + programming_percent3 + programming_percent4)/4
# print("Your final score is:", overall_grade, '%')

''' Calculates the overall grade for a course with three equally
    weighted exams (graded out of 100) that account for 60% of 
    the overall grade and four equally weighted programming 
    assignments (graded out of 50) that account for 40% of the 
    overall grade
'''

exam1_score = float(input("Enter exam 1 score: "))
exam2_score = float(input("Enter exam 2 score: "))
exam3_score = float(input("Enter exam 3 score: "))
programming_score1 = float(input("Enter programming score: "))
programming_score2 = float(input("Enter programming score: "))
programming_score3 = float(input("Enter programming score: "))
programming_score4 = float(input("Enter programming score: "))

avg_exam_scores = (exam1_score + exam2_score + exam3_score) / 3
prog_percent1 = (programming_score1/50) *100
prog_percent2 = (programming_score2/50) *100
prog_percent3 = (programming_score3/50) *100
prog_percent4 = (programming_score4/50) *100
avg_programming_scores = (prog_percent1 + prog_percent2 + prog_percent3 + prog_percent4) / 4
overall_grade = (avg_exam_scores * 0.6) + (avg_programming_scores * 0.4)

print("Your overall grade is: ", overall_grade)