# Author: Parul Mahajan
# Date: 11/11/2023
# Description: In this file, there is a class named
# Product to store information related to the product the user wishes to order.

class SmartProduct:
    def __init__(self, product_id, name, units, unitPrice):
        self.__product_id = product_id
        self.__name = name
        self.__units = units
        self.__unitPrice = unitPrice
        self.__totalCost = self.__units * self.__unitPrice

    # getter and setter for product ID
    def getProductId(self):
        return self.__product_id

    def setProductId(self, product_id):
        self.__product_id = product_id

    # getter and setter for product name
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # getter and setter for product units
    def getUnits(self):
        return self.__units

    def setUnits(self, units):
        self.__units = units
        self.__update_total_cost()

    # getter and setter for unitPrice
    def getUnitPrice(self):
        return self.__unitPrice

    def setUnitPrice(self, unitPrice):
        self.__unitPrice = unitPrice
        self.__update_total_cost()

    # getter and setter for totalCost
    def getTotalCost(self):
        return self.__totalCost

    def setTotalCost(self, totalCost):
        self.__totalCost = totalCost

    # private method to update total cost
    def __update_total_cost(self):
        self.__totalCost = self.__units * self.__unitPrice



