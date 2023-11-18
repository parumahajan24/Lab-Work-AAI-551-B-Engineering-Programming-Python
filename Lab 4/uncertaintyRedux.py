# Author: Parul Mahajan
# Date: 9/30/2023
# Description: Plays a position guessing game with the user.
# The user has to guess particle's position with 3 chances to do so.
# Using while loop, the program prints the correct output.

partXPos = 4
partYPos = 6
numberOfUserGuesses = 3

while numberOfUserGuesses >= 0:
    if numberOfUserGuesses == 0:
        print("Oh no! You ran out of chances. (4,6) was the particle's position!")
        numberOfUserGuesses = 3
        continue
    # tell user the number of chances they have left
    print(
        f"The particle is somewhere in this space! You have {numberOfUserGuesses} chances to guess it."
    )
    userXPos = int(input("What do you think its x coordinate is [1-10]? "))
    userYPos = int(input("What do you think its y coordinate is [1-10]? "))
    # If the position is the same, tell the user they found the particle
    if userXPos == partXPos and userYPos == partYPos:
        print("Good guess! (%d,%d) was the position!" % (partXPos, partYPos))
        break
    if userXPos > partXPos:
        print("Bad luck! The particle's x position is less than your x position!")
    if userXPos < partXPos:
        print("Bad luck! The particle's x position is greater than your x position!")
    if userYPos > partYPos:
        print("Bad luck! The particle's y position is less than your y position!")
    if userYPos < partYPos:
        print("Bad luck! The particle's y position is greater than your y position!")
    # decrement the number of changes by 1
    numberOfUserGuesses -= 1
