students = {
    101: {"Name": "Aarav", "Marks": [85, 90, 88]},
    102: {"Name": "Diya", "Marks": [92, 89, 95]},
    103: {"Name": "Rohan", "Marks": [78, 82, 80]},
}
def calculate_results(marks):
    """Receives a list of marks, calculates and returns total and average."""
    total = sum(marks)
    average = total / len(marks) if marks else 0.0
    return total, average

def display_student(roll, student):
    """Computes results and prints formatted details for a single student."""
    total, average = calculate_results(student["Marks"])
    print(
        f"Roll No: {roll} | Name: {student['Name']} | "
        f"Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}"
    )

def add_student(records, roll, name, marks):
    """Adds a new student if the roll number does not already exist."""
    if roll in records:
        print(f"Error: Roll number {roll} already exists!")
    else:
        records[roll] = {"Name": name, "Marks": marks}
        print(f"Student '{name}' (Roll No: {roll}) added successfully.")

def main():
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Display All Students")
        print("2. Add New Student")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\n--- All Student Records ---")
            for roll, student_data in students.items():
                display_student(roll, student_data)

        elif choice == "2":
            try:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Student Name: ").strip()
                marks = []
                for i in range(1, 4):
                    mark = int(input(f"Enter marks for Subject {i}: "))
                    marks.append(mark)
                add_student(students, roll, name, marks)
            except ValueError:
                print(
                    "Invalid input! Please enter numeric values for roll number and marks."
                )

        elif choice == "3":
            try:
                roll = int(input("Enter Roll Number to search: "))
                student_data = students.get(roll)
                if student_data:
                    print("\n--- Student Found ---")
                    display_student(roll, student_data)
                else:
                    print(f"Student with Roll Number {roll} not found.")
            except ValueError:
                print("Invalid input! Roll number must be an integer.")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option (1-4).")


if __name__ == "__main__":
    main()