# Author: Parul Mahajan
# Date: 10/7/2023
# Description: This module calculates the total surface area of a square pyramid after
# calculating the side area of 4 triangles
import math


# function definitions
def calcBaseArea(side):
    return side ** 2

# side area = the sum of the areas of all four triangles = 2 * a * Math.sqrt((a ** 2 / 4) + h ** 2)
def calcSideArea(side, height):
    return 2 * side * math.sqrt((side ** 2 / 4) + height ** 2)

def prntSurfArea(base_area, side_area):
    total_area = base_area + side_area
    print(f"The total surface area of the square pyramid is {total_area} square feet.")

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area} square feet.")

    side_area = calcSideArea(side, height)
    print(f"Total surface area of all four sides of the square pyramid is {side_area} square feet.")

    prntSurfArea(base_area, side_area)


main()
