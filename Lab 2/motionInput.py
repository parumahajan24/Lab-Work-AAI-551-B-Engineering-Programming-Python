# Author: Parul Mahajan
# Date: 9/16/2023
# Description: Given a duration of time, this program computes
# the velocity, average velocity, and displacement of an object.

# Useful values:
acceleration = 5.25
initialVelocity = 8.25

# Input time: time = 10.0
time = float(input("Please enter the elapsed time:"))

# Calculate the properties of the object:
# Compute the velocity.
velocity = initialVelocity + acceleration * time

# Compute the average velocity.
averageVelocity = initialVelocity + 1/2 * (acceleration * time)

# Compute the displacement of an object.
displacementOfObject = initialVelocity * time + 1/2 * (acceleration * pow(time, 2))


# Print the results:
print(f"time = {time} \n\nvelocity \t\t = {velocity} \naverage velocity = {averageVelocity} \ndisplacement \t = {displacementOfObject}")

