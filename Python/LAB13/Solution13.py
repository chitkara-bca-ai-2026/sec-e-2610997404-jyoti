print("="*50)
print("inventory control tool")
print("="*50)

#Intialize Inventory:
inventory = ["Notebook", "Pen", "Eraser", "Ruler", "Marker"]

#Function to display the inventory
def display_inventory():
    print("Current Inventory:")
    for item in inventory:
        print("- " + item)
#1.View 2.Add Item3. Remove Item 4.Sort 5.Exit
while True:
  Choice = int(input("Enter your choice (1-5): "))

#choice 1: View Inventory
  if Choice == 1:
    display_inventory()
#choice 2: Add Item
  elif Choice == 2:
    new_item = input("Enter the item to add: ")
    inventory.append(new_item.title())
    print(f"{new_item} has been added to the inventory.")
    display_inventory()
#choice 3: Remove Item
  elif Choice == 3:
    remove_item = input("Enter the item to remove: ")
    if remove_item in inventory:
        inventory.remove(remove_item.title())
        print(f"{remove_item} has been removed from the inventory.")
    else:
        print(f"{remove_item} is not in the inventory.")
    display_inventory()
#choice 4: Sort Inventory
  elif Choice == 4:
    inventory.sort()
    print("Inventory has been sorted.")
    display_inventory()
#choice 5: Exit
  elif Choice == 5:
    print("Exiting the Inventory Control System.")
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")