# Author: Parul Mahajan
# Date: 10/20/2023
# Description: This file defines all the required fucntions - read_config_state(), simulate_outbreak(), and plot_simulation_results()

import matplotlib.pyplot as plt
def output_region_state(region, day):
    """
    Reads in region and day, and outputs the entire state of the region and the day number
    :param region: A list representing the region in simulation
    :param day: A number representing how long the outbreak lasted
    """
    print(f"Day: {day}")
    for row in region:
        print(' '.join(str(cell) if isinstance(cell, dict) else cell for cell in row))
    print()
def read_config_file(region):
    """
    Reads in and store simulations initial configuration data from a file (txt file)

    :param region: A list representing the region in the simulation
    :return: A tuple containing a threshold data, infectious period and the updated region.
    """
    while True:
        try:
            fileName = input("Please enter the name of the region file: ")
            #  please update the input file and filepath as required.
            filepath = "C:\\Users\\pmahaja4\\Desktop\\Python AAI 551\\project1\\"
            filepath += fileName
            print(filepath)

            with open(filepath, 'r') as file:
                # Reading threshold for infection
                threshold_line = file.readline().strip().split(":")
                threshold = int(threshold_line[1])
                # print(threshold_line)

                # Reading infectious period
                infectious_period_line = file.readline().strip().split(":")
                infectious_period = int(infectious_period_line[1])
                # print(infectious_period)

                if threshold_line[0] != "Threshold":
                    raise ValueError("File format is incorrect.")
                if infectious_period_line[0] != "Infectious Period":
                    raise ValueError("File format is incorrect")

                # Reading the region's health states
                for line in file:
                    #  values in row are comma separated
                    row = [char.strip() for char in line.strip().split(",")]

                    # Valid health states - s,i,r,v
                    for state in row:
                        if state not in ["s", "i", "r", "v"]:
                          raise ValueError(f"Invalid health state detected: {state}")
                    region.append(row)

                # call the function to print the Day 0 scenario
                # output_region_state(region, 0)
                return threshold, infectious_period

        except FileNotFoundError:
            print("The file does not exist. Please enter a valid file name.")
        except ValueError as ve:
            print("Error:", ve)
            exit(-1)
        except Exception as e:
            print("Something went wrong with the input file:", str(e))
            exit(-2)

# initialize Region as list and call the initial function read-config_file(region)
# region = []
# threshold, infectious_period = read_config_file(region)


def get_neighbors(region, row, col):
    neighbors = []
    for i in range(max(0, row - 1), min(len(region), row + 2)):
        for j in range(max(0, col - 1), min(len(region[0]), col + 2)):
            if (i, j) != (row, col):
                neighbors.append(region[i][j])
    return neighbors

def simulate_outbreak(region, threshold, infectious_period, susceptible_counts, infectious_counts, recovered_counts):
    """
    Simulates the outbreak within the region
    :param region: A list representing the region in the simulation
    :param threshold: A number representing the threshold for the infection as given in the file
    :param infectious_period: A number representing for how long a person will be infected OR after how many days a person will recover.
    :param susceptible_counts: A number representing susceptible count for the infected simulation
    :param infectious_counts: A number representing infectious count for the infected simulation
    :param recovered_counts: A number representing recovered count for the infected simulation
    :return: the number of days the outbreak lasted
    """
    days = 0
    peak_infectious_count = 0
    peak_day = 0

    # Initialize counts for Day 0
    initial_susceptible = sum(row.count('s') for row in region)
    initial_infectious = sum(row.count('i') for row in region)
    initial_recovered = sum(row.count('r') for row in region)

    susceptible_counts.append(initial_susceptible)
    infectious_counts.append(initial_infectious)
    recovered_counts.append(initial_recovered)

    # Print initial state of the region
    output_region_state(region, 0)

    while 'i' in [state for row in region for state in row]:
        new_region = [row.copy() for row in region]
        for row in range(len(region)):
            for col in range(len(region[row])):
                if region[row][col] == 's':
                    infectious_neighbors = sum(1 for neighbor in get_neighbors(region, row, col) if neighbor == 'i')
                    if infectious_neighbors >= threshold:
                        new_region[row][col] = 'i'
                elif region[row][col] == 'i':
                    if 'infectious_days' not in locals():
                        infectious_days = {}
                    if (row, col) not in infectious_days:
                        infectious_days[(row, col)] = 1
                    else:
                        infectious_days[(row, col)] += 1
                    if infectious_days[(row, col)] >= infectious_period:
                        new_region[row][col] = 'r'

        region = new_region
        days += 1
        # output_region_state(region,days)

        # Update and print counts for the current day
        susceptible = sum(row.count('s') for row in region)
        infectious = sum(row.count('i') for row in region)
        recovered = sum(row.count('r') for row in region)

        susceptible_counts.append(susceptible)
        infectious_counts.append(infectious)
        recovered_counts.append(recovered)

        # Update peak infectious count and day
        if infectious > peak_infectious_count:
            peak_infectious_count = infectious
            peak_day = days

        # Print the current state of the region
        print(f"Day {days}")
        for row in region:
            print(' '.join(row))
        print()

    print("Final state of the region:")
    for row in region:
        print(' '.join(row))
    print()

    print(f"Outbreak Duration: {days} days")
    print(f"Peak Day: Day {peak_day}")
    print(f"Peak Infectious Count: {peak_infectious_count} people")

    return days, susceptible_counts,infectious_counts,recovered_counts

# days, susceptible_counts, infectious_counts, recovered_counts = simulate_outbreak(region, threshold, infectious_period,[], [], [])

def plot_simulation_results(susceptible_counts, infectious_counts, recovered_counts, outbreak_duration):
    """
    Graph the diagram or plot for the result os simulation - A single line plot
    :param susceptible_counts: A number representing susceptible count for the region of simulation
    :param infectious_counts: A number representing infectious count for the region of simulation
    :param recovered_counts: A number representing recovered count for the region of simulation
    :param outbreak_duration: A number representing how long the outbreak lasted - no. of days
    """
    if len(susceptible_counts) != len(infectious_counts) or len(susceptible_counts) != len(recovered_counts):
        print("Error: The lists of counts are not of the same length.")
        return

    if outbreak_duration != len(susceptible_counts) - 1:
        print(f"Error: outbreak_duration is {outbreak_duration}, but should be {len(susceptible_counts) - 1}.")
        return

    days = list(range(outbreak_duration + 1))
    # print("days..",days)

    # plotting the graph
    plt.figure(figsize=(10, 5))
    plt.plot(days, susceptible_counts, label='S', marker='o')
    plt.plot(days, infectious_counts, label='I', marker='o')
    plt.plot(days, recovered_counts, label='R', marker='o')

    plt.title('SIR State Counts')
    plt.xlabel('Days')
    plt.ylabel('COunts')
    plt.legend()
    plt.grid(True)
    plt.show()

# plot_simulation_results(susceptible_counts,infectious_counts,recovered_counts,days)



