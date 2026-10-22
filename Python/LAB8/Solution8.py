import sys

# Display Header
print("========================================")
print("        SCHOOL RESULT PROCESSING        ")
print("========================================")

# 1. Accept student details
student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number   : ")

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

total_marks = 0.0
has_failed_subject = False

# 2. Input marks for 5 subjects using a loop
for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    
    # Validate marks range
    if marks < 0 or marks > 100:
        print("\nError: Marks must be between 0 and 100.")
        sys.exit()
        
    # Check passing status (below 40 is failed)
    if marks < 40:
        has_failed_subject = True
        
    total_marks += marks

# 3. Calculate total and percentage
percentage = (total_marks / 500) * 100

# 4. Assign Grade & Remark
if has_failed_subject:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"

# 5. Display Formatted Student Report Card
print("\n========================================")
print("          STUDENT REPORT CARD           ")
print("========================================")
print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print("----------------------------------------")
print(f"Total Marks  : {total_marks:.1f} / 500.0")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remarks}")
print("========================================")