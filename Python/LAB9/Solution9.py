# File Name: lab09_festival_patterns.py

# 1. Take input from the user for the number of rows
n = int(input("Enter the number of rows: "))
print()  # Empty line for formatting

# ----------------------------------------------------
# Pattern 1: Star Triangle (Right-Angled)
# ----------------------------------------------------
print("Pattern 1: Star Triangle")
print("-" * 33)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
print()

# ----------------------------------------------------
# Pattern 2: Number Triangle
# ----------------------------------------------------
print("Pattern 2: Number Triangle")
print("-" * 33)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print numbers separated by spaces
        print(j, end=" ")
    print()
print()

# ----------------------------------------------------
# Pattern 3: Inverted Star Triangle
# ----------------------------------------------------
print("Pattern 3: Inverted Star Triangle")
print("-" * 33)
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print()

# ----------------------------------------------------
# Pattern 4: Pyramid (Centered Triangle)
# ----------------------------------------------------
print("Pattern 4: Pyramid")
print("-" * 33)
for i in range(1, n + 1):
    # Nested loop for printing spaces
    for j in range(n - i):
        print(" ", end="")
    # Nested loop for printing stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()