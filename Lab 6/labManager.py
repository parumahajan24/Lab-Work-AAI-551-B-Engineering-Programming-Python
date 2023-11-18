# Author: Parul Mahajan
# Date: 10/13/2023
# Description: Program manages a small laboratory’s equipment inventory (max capacity 5) and asks user 4 options
# to add,remove,display or leave the lab manager with appropriate messages after each operation

equipment_list = []
def displayMenu():
    print("\nYou can choose from the following options:")
    print("1. Add Equipment")
    print("2. Remove Equipment")
    print("3. Display Current Equipment")
    print("4. Leave the Laboratory Manager")

print("Welcome to the inventory manager for your laboratory!")

while True:
    displayMenu()
    choice = input("What would you like to do: ")

    if choice == '1':
        if len(equipment_list) < 5:
            equipment = input("What would you like to add to the laboratory: ")
            equipment_list.append(equipment)
            print(f"{equipment} has been added.")
        else:
            print("Your laboratory cannot support any more equipment!")
    elif choice == '2':
        equipment_to_remove = input("What would you like to remove from the laboratory: ")
        if equipment_to_remove in equipment_list:
            equipment_list.remove(equipment_to_remove)
            print(f"{equipment_to_remove} has been removed.")
        else:
            print(f"{equipment_to_remove} was not present and could not be removed.")
    elif choice == '3':
        print("Your laboratory currently contains:", end="")
        for equipment in equipment_list:
            print(f" {equipment} ", end="")
        print()
    elif choice == '4':  # Leave the Laboratory Manager
        print("Good luck on your journey of discovery!")
        break

    else:
        print(f"{choice} was not a valid option. Please try again")



