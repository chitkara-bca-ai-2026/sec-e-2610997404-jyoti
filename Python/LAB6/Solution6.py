# Clothing Store Billing System

# Step 1-4: Accept inputs from the user
customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

# Step 5: Calculate total cost
total_amount = price * quantity

# Step 6: Display the bill matching the expected output format
print("\n======================================")
print("                 BILL                 ")
print("======================================")
print(f"Customer Name  : {customer_name}")
print(f"Garment Name   : {garment_name}")
print(f"Price per Unit : Rs. {price}")
print(f"Quantity       : {quantity}")
print(f"Total Amount   : Rs. {total_amount}")
print("======================================")