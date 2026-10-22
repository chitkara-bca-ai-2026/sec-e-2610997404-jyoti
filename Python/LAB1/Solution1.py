print("==============================================")
print("              STUDENT FEE CALCULATOR")
print("==============================================")

# Step 1: Ask for fee values
tuition_fee = float(input("Enter Tuition Fee: Rs "))
lab_fee = float(input("Enter Lab Fee: Rs "))
library_fee = float(input("Enter Library Fee: Rs "))
exam_fee = float(input("Enter Exam Fee: Rs "))
discount = float(input("Enter Discount Amount: Rs "))

# STEP 3: Add all values
print("\n==============================================")
print("STEP 3: ADD ALL FEE VALUES")
print("==============================================")
total_fee = tuition_fee + lab_fee + library_fee + exam_fee
print("Total Fee (Tuition + Lab + Library + Exam): Rs", total_fee)

# STEP 4: Subtract discount
print("\n==============================================")
print("STEP 4: SUBTRACT DISCOUNT")
print("==============================================")
final_fee = total_fee - discount
print("Final Fee (Total Fee - Discount): Rs", final_fee)

# STEP 5: Make it annual
print("\n==============================================")
print("STEP 5: CALCULATE ANNUAL FEE")
print("==============================================")
annual_fee = final_fee * 2
print("Annual Fee (Final Fee * 2 semesters): Rs", annual_fee)

# STEP 6: Divide by 12
print("\n==============================================")
print("STEP 6: CALCULATE MONTHLY PAYMENT")
print("==============================================")
monthly_payment = annual_fee / 12
print("Monthly Payment (Annual Fee / 12): Rs", round(monthly_payment, 2))

print("\n-------------- Calculations --------------")
print("Total Fee (before discount): Rs", total_fee)
print("Final Fee (after discount): Rs", final_fee)
print("Annual Fee (2 semesters): Rs", annual_fee)
print("Monthly Installment: Rs", round(monthly_payment, 2))

# Fee Summary
print()
print("==============================================")
print("                 FEE SUMMARY")
print("==============================================")

print("Tuition Fee      : Rs", tuition_fee)
print("Lab Fee          : Rs", lab_fee)
print("Library Fee      : Rs", library_fee)
print("Exam Fee         : Rs", exam_fee)
print("Total Fee        : Rs", total_fee)
print("Discount         : Rs", discount)
print("Final Fee        : Rs", final_fee)
print("Annual Fee       : Rs", annual_fee)
print("Monthly Payment  : Rs", round(monthly_payment, 2))
print("==============================================")