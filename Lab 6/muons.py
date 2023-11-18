# Author: Parul Mahajan
# Date: 10/13/2023
# Description: simulating an array of CRMD’s on a two-dimensional map,
# then finding the location with the highest capture rate and the location with the
# lowest capture rate and outputting the entire map as a grid.

import random
MAP_DIMENSION = 8

captureMap = [[0 for _ in range(MAP_DIMENSION)] for _ in range(MAP_DIMENSION)]

highestCapture = -1
lowestCapture = float('inf')
highestX = None
highestY = None
lowestX = None
lowestY = None

# Fill map with random values in the range of 0-500
for x in range(MAP_DIMENSION):
    for y in range(MAP_DIMENSION):
        captureMap[x][y] = random.randint(0, 500)

for x in range(MAP_DIMENSION):
    for y in range(MAP_DIMENSION):
        value = captureMap[x][y]
        if value > highestCapture:
            highestCapture = value
            highestX = x + 1
            highestY = y + 1
        if value < lowestCapture:
            lowestCapture = value
            lowestX = x + 1
            lowestY = y + 1

# Print the highest and lowest capture rates & their coordinates
print(f"The highest capture rate was {highestCapture} at location {highestX}, {highestY}")
print(f"The lowest capture rate was {lowestCapture} at location {lowestX}, {lowestY}")

print("\nThe map looks like the following:")
for x in range(MAP_DIMENSION):
    for y in range(MAP_DIMENSION):
        print(f"{captureMap[x][y]:<4}", end=" ")
    print()


