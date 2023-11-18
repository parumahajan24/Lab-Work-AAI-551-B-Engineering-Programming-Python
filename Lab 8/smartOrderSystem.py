# Author: Parul Mahajan
# Date: 11/11/2023
# Description: In this file, a private function that calculates the totalCost, stores the totalCost
# and then defines a main function to prompt user for name and units and output the TotalCost

from SmartProduct import SmartProduct


def calcTotal(products):
    totalProducts = 0
    for product in products:
        totalProducts += product.getTotalCost()
    return totalProducts


def main():
    products = []
    numProducts = int(input("How many products would you like to order: "))

    for i in range(numProducts):
        # generate a unique product ID
        product_id = i + 1
        name = input("Please enter the name of the product you wish to order: ")
        units = int(input("Please enter the number of units of product you wish to order: "))
        product = SmartProduct(product_id, name, units, 9.99)
        products.append(product)

    totalCost = calcTotal(products)

    print("You ordered:")
    for product in products:
        print(f"ID: {product.getProductId()}")
        print(f"Name: {product.getName()}")
        print(f"Units: {product.getUnits()}")
        print(f"Price: ${product.getUnitPrice():.2f}")
        print(f"Total Cost : ${product.getTotalCost():.2f}")

    print(f"\nThe total cost of your order is: ${totalCost:.2f}")


if __name__ == "__main__":
    main()
