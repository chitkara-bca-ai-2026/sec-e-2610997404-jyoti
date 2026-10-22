import sys

# Display Header
print("========================================")
print("      CALENDAR VERIFICATION SYSTEM      ")
print("========================================")

# Take input from user
year = int(input("Enter year: "))

# Input validation
if year <= 0:
    print("\nError: Year must be a positive integer greater than 0.")
    sys.exit()

# Check leap year rules and determine details
if year % 100 == 0:
    if year % 400 == 0:
        is_leap = True
        reason = "Century year divisible by 400"
    else:
        is_leap = False
        reason = "Century year not divisible by 400"
else:
    if year % 4 == 0:
        is_leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap = False
        reason = "Not divisible by 4"

# Set days based on leap year status
if is_leap:
    status = "LEAP YEAR"
    total_days = 366
    feb_days = 29
else:
    status = "COMMON YEAR"
    total_days = 365
    feb_days = 28

# Display Results
print("----------------------------------------")
print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {total_days} days")
print(f"Days in February: {feb_days} days")
print(f"Reason: {reason}")
print("----------------------------------------")