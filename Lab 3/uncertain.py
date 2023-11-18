# Author: Parul Mahajan
# Date: 9/23/2023
# Description: This program ask user to guess coordinate and responds back with a Yay, Nay or Wrong input

x_coordinate = 4
y_coordinate = 6

userInput_xCoordinate = int(input("The particle is somewhere in this space! What do you think its x coordinate is ["
                                  "1,10]? "))
userInput_yCoordinate = int(input("What do you think its y coordinate is [1,10]? "))

if x_coordinate == userInput_xCoordinate and y_coordinate == userInput_yCoordinate:
    print("Good guess! (4,6) was the position!")
elif userInput_xCoordinate not in range(1, 11) or userInput_yCoordinate not in range(1, 11):
    print(f"No good! {userInput_xCoordinate, userInput_yCoordinate} is outside of the range!")
else:
    print("Bad Luck! (4,6) was the position!")
