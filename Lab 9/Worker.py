# Author: Parul Mahajan
# Date: 11/18/2023
# Description: This module defines a class named Worker which inherits Employee and will store
# information regarding a worker type employee.

from Employee import Employee


class Worker(Employee):
    def __init__(self, emp_name, emp_id, pay_rate, shift):
        super().__init__(emp_name, emp_id, pay_rate)
        self.__shift = shift

    # getter/setter for shift
    def getShift(self):
        return self.__shift

    def setShift(self, shift):
        self.__shift = shift
