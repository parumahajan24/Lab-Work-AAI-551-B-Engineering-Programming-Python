# Author: Parul Mahajan
# Date: 10/13/2023
# Description: creates a simple graph using matplotlib to show temperatures of three cities, NYC, Stamford, and New Jersey

import matplotlib.pyplot as plt
import random

# Create a list to represent time 1 though 12, inclusive
time = list(range(1, 13))

# Define the names of three cities
cities = ["NYC", "Stamford", "New Jersey"]

# Initialize lists to store temperatures for each city
city_temperatures = []

# Generate random temperatures for each city and append them to the respective lists
for city in cities:
    temperatures = [random.randint(10, 30) for _ in range(12)]
    city_temperatures.append(temperatures)

# Create a line graph for each city's temperatures
for i in range(len(cities)):
    plt.plot(time, city_temperatures[i], label=cities[i])

# Add title and labels to the graph
plt.title('Hourly Temperatures')
plt.xlabel('Hours')
plt.ylabel('Temperature (°C)')

# Create a legend using the city names
plt.legend()

# Display the graph
plt.show()
