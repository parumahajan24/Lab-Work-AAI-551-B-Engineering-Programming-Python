# Author: Parul Mahajan
# Date: 9/23/2023
# Description: This program prompts user to enter a number between [1,9] and outputs the equivalent Roman Numeral

user_input = int(input("Please enter a number between 1 and 9 to convert to a roman numeral: "))
if user_input == 1:
    print("\u2160")
elif user_input == 2:
    print("\u2161")
elif user_input == 3:
    print("\u2162")
elif user_input == 4:
    print("\u2163")
elif user_input == 5:
    print("\u2164")
elif user_input == 6:
    print("\u2165")
elif user_input == 7:
    print("\u2166")
elif user_input == 8:
    print("\u2167")
elif user_input == 9:
    print("\u2168")
elif user_input not in range(1, 10):
    print(f"{user_input} is outside the allowed range of 1-9")
