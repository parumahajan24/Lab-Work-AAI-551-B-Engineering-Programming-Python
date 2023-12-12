# Author: Parul Mahajan
# Date: 10/22/2023
# Description: This file imports the SimLibrary.py file and calls the function to read and store configuration file, execute simualtion_outbrak
# and to plot the result of simulation from SimLibrary.py file

# Importing the SimLibrary module
import SimLibrary

def main():
    # Declaring an empty List to store the region
    region = []

    # Declaring three empty Lists to store the daily counts of susceptible, infectious, and recovered individuals
    susceptible_counts = []
    infectious_counts = []
    recovered_counts = []

    # Calling the function to read in and store the configuration file
    # This function should return the infection threshold
    infection_threshold,infectious_period = SimLibrary.read_config_file(region)

    # Calling the function to execute the simulation
    # This function should return the outbreak duration
    outbreak_duration, susceptible_counts, infectious_counts,recovered_counts = SimLibrary.simulate_outbreak(region, infection_threshold,infectious_period , [],[],
                                                     [])

    # Calling the function to generate the plot of the outbreak
    SimLibrary.plot_simulation_results(susceptible_counts, infectious_counts, recovered_counts, outbreak_duration)


if __name__ == "__main__":
    main()
