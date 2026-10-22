# Print Header
print("========================================")
print("         STUDENT RECORD DISPLAY")
print("========================================")

# Take input from the user
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

print("----------------------------------------")
print("Student Details:")
print(f"  Name  : {name}")
print(f"  Age   : {age}")
print(f"  Marks : {marks:.1f}")
print("----------------------------------------")