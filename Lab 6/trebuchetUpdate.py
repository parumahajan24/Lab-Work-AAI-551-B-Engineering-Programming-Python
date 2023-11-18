# Author: Parul Mahajan
# Date: 10/13/2023
# Description: This program allows the user to enter in a number of distances
# that their trebuchet's projectile was thrown and then displays the top three
# distances to the user, and the distance and the trial numbers, are now only stored in the two List data structures

distances = [0,0,0]
trials = [0,0,0]

#Help determines if the user wishes to add in additional high distances
keepGoing = "Y"
trial = 1

#So long as keepGoing is Y, keep adding in more trials
while keepGoing == "Y":
    distance = int(input(f"Please enter your distance for trial {trial}: "))

    #If the new distance is farther than the farthest distance, replace it
    #and shift everything else down
    if distance > distances[0]:
        distances[2] = distances[1]
        distances[1] = distances[0]
        distances[0] = distance
        trials[2] = trials[1]
        trials[1] = trials[0]
        trials[0] = trial
    #If the new distance is distance than the second distance distance, replace it
    #and shift everything else down
    elif distance > distances[1]:
        distances[2] = distances[1]
        distances[1] = distance
        trials[2] = trials[1]
        trials[1] = trial
    #If the new distance is distance than the third distance distance, replace it
    elif distance > distance[2]:
        distances[2] = distance
        trials[2] = trial

    keepGoing = input("Would you like to input another trial? (Y/N):")

    trial += 1

#Output the highest distances and the initials of those people
print("The top three distances for the trebuchet are:")
print("Trial Distance")
print("%5d %8d" % (trials[0], distances[0]))
print("%5d %8d" % (trials[1], distances[1]))
print("%5d %8d" % (trials[2], distances[2]))
