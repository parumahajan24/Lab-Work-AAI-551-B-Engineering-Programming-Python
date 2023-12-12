# Author: Parul Mahajan
# Date: 11/18/2023
# Description: This module stores general employee
# data, the getter/setter and a calcPay function to return the pay (hours * pay_rate)

class Employee:
    def __init__(self, emp_name, emp_id, pay_rate):
        self._emp_name = emp_name
        self._emp_id = emp_id
        self._pay_rate = pay_rate

    def calcPay(self, hours):
        return hours * self._pay_rate

    # getter and setter for emp name
    def getName(self):
        return self._emp_name

    def setName(self, emp_name):
        self._emp_name = emp_name

    # getter and setter for emp id
    def getId(self):
        return self._emp_id

    def setId(self, emp_id):
        self._emp_id = emp_id

    # getter and setter for pay_rate
    def getPayRate(self):
        return self._pay_rate

    def setPayRate(self, pay_rate):
        self._pay_rate = pay_rate

