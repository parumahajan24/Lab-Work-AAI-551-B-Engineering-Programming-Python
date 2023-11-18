# Author: Parul Mahajan
# Date: 11/11/2023
# Description: In this file, a private function that calculates the totalCost, stores the totalCost
# and then defines a main function to prompt user for name and units and output the TotalCost

from Product import Product


def __calcTotal(product):
    # calculate total cost and update it in Product object
    total_cost = product.getUnits() * product.getUnitPrice()
    # directly accessing private variable
    product.setTotalCost(total_cost)


def main():
    product = Product("", 0, 9.99)

    # prompt user for product name and number of units
    name = input("Please enter the name of the product you wish to order: ")
    units = int(input("Please enter the number of units of product you wish to order: "))

    # store information in Product object
    product.setName(name)
    product.setUnits(units)

    # calculate and store the total price of the order
    __calcTotal(product)

    print("Your ordered:")
    print(f"Name: {product.getName()}")
    print(f"Units: {product.getUnits()}")
    print(f"Price: ${product.getUnitPrice():.2f}")
    print(f"Total Cost : ${product.getTotalCost():.2f}")


if __name__ == "__main__":
    main()
