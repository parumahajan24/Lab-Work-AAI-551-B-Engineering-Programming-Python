# Author: Parul Mahajan
# Date: 11/18/2023
# Description: This module defines the functionality which will manage the employees of a small
# company

from Worker import Worker
from Supervisor import Supervisor


def calcTotalPay(employees):
    total_pay = 0
    for i in employees:
        total_pay += i.calcPay(40)  # assuming 40 hours worked.
    return total_pay


def listEmployees(employees):
    for employee in employees:
        print(f"Name: {employee.getName()}\nID: {employee.getId()}\nPay Rate: ${employee.getPayRate()}")
        if isinstance(employee, Worker):
            shift = 'Day Shift' if employee.getShift() == 1 else 'Night Shift'
            print(f"Shift: {shift}")
        elif isinstance(employee, Supervisor):
            print(f"Level: {employee.getLevel()}")


def main():
    employees = []
    num_employees = int(input("How many employees would you like to add: "))

    i = 0
    while i < num_employees:
        employee_type = input("\nWould you like to add a worker or a supervisor: ").strip().lower()

        if employee_type in ["worker", "supervisor"]:
            emp_name = input(f"Please enter the name of the {employee_type}: ")
            emp_id = input(f"Please enter the id of the {employee_type}: ")
            pay_rate = float(input(f"Please enter the pay rate of the {employee_type}: "))

            if employee_type == "supervisor":
                level = int(input("Please enter the level of the supervisor: "))
                employees.append(Supervisor(emp_name, emp_id, pay_rate, level))
            elif employee_type == "worker":
                shift = int(input("Please enter the shift of the worker (1 for day, 2 for night): "))
                employees.append(Worker(emp_name, emp_id, pay_rate, shift))
            # increment only when a valid worker/supervisor is added
            i += 1
        else:
            print(f"{employee_type} is not a worker or supervisor. Try again!")

    listEmployees(employees)
    total_pay = calcTotalPay(employees)
    print(f"The total cost of all of the worker's pay is ${total_pay}")


if __name__ == "__main__":
    main()
