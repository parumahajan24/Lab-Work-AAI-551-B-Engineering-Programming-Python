# Author: Parul Mahajan
# Date: 11/18/2023
# Description: This module defines a class named Supervisor which inherits Employee and will
# store information regarding a supervisor type employee

from Employee import Employee


class Supervisor(Employee):
    def __init__(self, emp_name, emp_id, pay_rate, level):
        super().__init__(emp_name, emp_id, pay_rate)
        self.__level = level

    def calcPay(self, hours):
        return super().calcPay(hours) + 1000.00 * self.__level

    # getter/setter for level
    def getLevel(self):
        return self.__level

    def setLevel(self, level):
        self.__level = level
