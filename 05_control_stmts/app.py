# Student Grade Tracker Solution
# Variables - Operators - Control Statements


#  -> Student ID -> Student Name -> Attendance
Student_ID = int(input("Enter ID: "))
Student_Name = input("Enter Name: ")
Student_Attendance = int(input("Enter Attendance: "))

total_score = 0
num_of_scores = 0

continue_input = "yes"

while continue_input == "yes":
    current_score =  int(input(f"Enter Score {num_of_scores+1}: "))
    continue_input = input(" Do you want to enter another score ? (yes/no) ")
    # increment score count
    num_of_scores+=1
    # update the total score by adding current given score
    total_score = total_score + current_score

# Average Score
avg_score = total_score/num_of_scores

# Grade the student
if avg_score >= 85:
    grade = "A"
elif avg_score >= 70:
    grade = "B"
elif avg_score >= 50:
    grade = "C"
else:
    grade = "Fail"

# Attendance Criteria
attendance_status = "WARNING LOW Attendance" if Student_Attendance < 75 else "OK GOOD Attendance"

print("Student Details")
print("======================")
print("Student Name : ",Student_Name)
print("Student Id : ",Student_ID)
print("Student Attedance : ",Student_Attendance)
print(f"Student Number of scores : {num_of_scores}")
print(f"Student Total Score : {total_score}")
print(f"Student Average Score : {avg_score}")
print("student Attendance Status : ", attendance_status)
print(f"Student Grade : {grade}")

# Award Eligibility
if avg_score >= 85 and Student_Attendance > 75:
    print("Got Awarded")

