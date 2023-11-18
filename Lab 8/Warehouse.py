# Author: Parul Mahajan
# Date: 11/11/2023
# Description: This file defines a class, to store the information related to the goods

class Warehouse:
    def __init__(self, initialGoods):
        self.__totalGood = initialGoods

    # function to ask user no. of goods they want to add to warehouse
    def addGood(self):
        amount = int(input("How many goods would you like to add: "))
        self.__totalGood += amount

    # function to ask user no. of goods they want to remove to warehouse
    def removeGoods(self):
        amount = int(input("How many goods would you like to remove: "))
        if amount > self.__totalGood:
            print("You do not have that many goods!")
        else:
            self.__totalGood -= amount

    def getTotalGoods(self):
        return self.__totalGood
