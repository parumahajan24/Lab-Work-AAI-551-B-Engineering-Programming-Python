# Author: Parul Mahajan
# Date: 9/23/2023
# Description: This program prompts user to enter a number between [1,9] and outputs the equivalent Roman Numeral.

import random

distance = random.randint(0, 450)

if distance > 400:
    print(f"The ball flew {distance} feet and the batter scored a home run! That's one point for out team!")
# between 135 and 400 inclusively
elif distance in range(135, 401):
    print(f"The ball flew {distance} feet and the batter made it to third base!")
# between 10 and 134 inclusively
elif distance in range(10, 135):
    print(f"The ball flew {distance} feet and the batter made it to second base!")
# between 1 and 9 inclusively
elif distance in range(1, 10):
    print(f"The ball flew {distance} feet because the batter bunted, and made it to first base!")
elif distance == 0:
    print("The batter has made a strike! Oh no!")
