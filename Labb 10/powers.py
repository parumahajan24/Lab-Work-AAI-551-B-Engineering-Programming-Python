# Author: Parul Mahajan
# Date: 12/2/2023
# Description:This program calculates the result of a user specified base value being put to a user specified exponent.

def powers(base, exponent):
    print(f"powers({base}, {exponent})")
    if exponent == 1:
        return base
    else:
        return base * powers(base, exponent - 1)


def main():
    base = int(input("Please enter the base value: "))
    exponent = int(input("Please enter the exponent value: "))
    result = powers(base, exponent)
    print(f"{base} ^ {exponent} is {result}")


if __name__ == "__main__":
    main()
