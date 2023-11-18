# Author: Parul Mahajan
# Date: 11/11/2023
# Description: In this file, we call a main function where we define the object of Warehouse
# and prompt user for options to choose from, to add, remove, output or quit

from Warehouse import Warehouse


def main():
    # initializing object of Warehouse with 0 goods
    warehouse = Warehouse(0)

    while True:
        print("""Please select from the following options:
                 1: Add Goods
                 2: Remove Goods
                 3: Output Total Goods 
                 4: Quit """)

        choice = input("Choice: ")

        if choice == '1':
            warehouse.addGood()
        elif choice == '2':
            warehouse.removeGoods()
        elif choice == '3':
            totalGoods = warehouse.getTotalGoods()
            print(f"There are {totalGoods} in the warehouse.")
        elif choice == '4':
            print("Good Bye!")
            break
        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()

