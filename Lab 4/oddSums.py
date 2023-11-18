# Author: Parul Mahajan
# Date: 9/30/2023
# Description: Generates a random number between (1,10) and (11,20), inclusively
# Using for loop, calculates the sum of all odd numbers,
# includes the randomly generated numbers to calculate the sum if they are odd.

import random

# generate random integer between (1,10) and (11,20), inclusively
num1 = random.randint(1, 10)
num2 = random.randint(11, 20)

# initialize the variable to store the sum
oddSum = 0

for i in range(num1, num2 + 1):
    if i % 2 != 0:
        oddSum += i

print(
    f"The first random number was {num1}, the second random number was {num2}, and the sum is {oddSum}"
)
