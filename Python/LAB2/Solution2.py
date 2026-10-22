# Lab 02 - Employee Information System

# 1. Employee Name
name = input("Enter Employee Name: ")
print("  Data type:", type(name))


# 2. Employee ID
employee_id = int(input("Enter Employee ID: "))
print("  Data type:", type(employee_id))


# 3. Salary
salary = float(input("Enter Salary: "))
print("  Data type:", type(salary))


# 4. Department
department = input("Enter Department: ")
print("  Data type:", type(department))


# 5. Employee Active Status
active_input = input("Is the employee active? (yes/no): ")
active = active_input.lower() == "yes"
print("  Data type:", type(active))


# Display all employee details
print("\n--- Employee Details ---")
print("Name       :", name)
print("ID         :", employee_id)
print("Salary     :", salary)
print("Department :", department)
print("Active     :", active)