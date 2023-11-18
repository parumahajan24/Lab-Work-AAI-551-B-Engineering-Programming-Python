# Author: Parul Mahajan
# Date: 9/30/2023
# Description: It records distances the projectile files for a number of trials, and keep track of the three
# trials with the furthest distance

# top 3 distances
firstDistance = 0
secondDistance = 0
thirdDistance = 0

# trial number of top 3 distances
firstTrialDistance = 0
secondTrialDistance = 0
thirdTrialDistance = 0

additionalTrials = "Y"
currentTrialNumber = 1

while additionalTrials == "Y":
    tempDistance = int(
        input("Please enter your distance for trial %d: " % currentTrialNumber)
    )
    # Compare with existing top distances
    if tempDistance > firstDistance:
        thirdDistance, secondDistance, firstDistance = (
            secondDistance,
            firstDistance,
            tempDistance,
        )
        thirdTrialDistance, secondTrialDistance, firstTrialDistance = (
            secondTrialDistance,
            firstTrialDistance,
            currentTrialNumber,
        )
    elif tempDistance > secondDistance:
        thirdDistance, secondDistance = secondDistance, tempDistance
        thirdTrialDistance, secondTrialDistance = (
            secondTrialDistance,
            currentTrialNumber,
        )
    elif tempDistance > thirdDistance:
        thirdDistance = tempDistance
        thirdTrialDistance = currentTrialNumber
    additionalTrials = input("Would you like to input another trial? (Y/N): ")
    currentTrialNumber = currentTrialNumber + 1

print("The top three distances for the trebuchet are:")
print("{:<10} {:<10}".format("Trial", "Distance"))
if firstTrialDistance != 0:
    print("{:<10} {:<10}".format(firstTrialDistance, firstDistance))
if secondTrialDistance != 0:
    print("{:<10} {:<10}".format(secondTrialDistance, secondDistance))
if thirdTrialDistance != 0:
    print("{:<10} {:<10}".format(thirdTrialDistance, thirdDistance))
