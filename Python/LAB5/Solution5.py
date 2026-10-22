import math

# Header
print("========================================")
print("       ENGINEERING CALCULATION TOOL     ")
print("========================================")

# User Inputs
val = float(input("Enter a numerical value: "))
exp = float(input("Enter an exponent: "))
dec_val = float(input("Enter a decimal measurement: "))

# Calculations
power_res = math.pow(val, exp)
sqrt_res = math.sqrt(val)
ceil_res = math.ceil(dec_val)
floor_res = math.floor(dec_val)

# Output Results
print("\n--- Results ---")
print(f"Value               : {val:.1f}")
print(f"Exponent            : {exp:.1f}")
print(f"Power (pow)         : {power_res:.1f}")
print(f"Square Root (sqrt)  : {sqrt_res:.4f}")
print(f"Decimal Value       : {dec_val}")
print(f"Ceil Value          : {ceil_res}")
print(f"Floor Value         : {floor_res}")
print("========================================")