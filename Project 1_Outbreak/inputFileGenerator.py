# Author: Parul Mahajan
# Date: 10/23/2023
# Description: This file asks user for various input to generate ragion file

def generate_region(dimensions, total_population, infectious_people, vaccinated_people):
    if infectious_people + vaccinated_people > total_population:
        print("Error: The sum of infectious and vaccinated people exceeds the total population.")
        return None

    region = [['s'] * dimensions for _ in range(dimensions)]

    # Infect some people randomly
    for _ in range(infectious_people):
        while True:
            x, y = randint(0, dimensions - 1), randint(0, dimensions - 1)
            if region[x][y] == 's':
                region[x][y] = 'i'
                break

    # Vaccinate some people randomly
    for _ in range(vaccinated_people):
        while True:
            x, y = randint(0, dimensions - 1), randint(0, dimensions - 1)
            if region[x][y] == 's':
                region[x][y] = 'v'
                break
    return region

def write_input_file(filename, region, infection_threshold, infectious_period):
    with open(filename, 'w') as f:
        f.write(f"{len(region)}\n")
        f.write(f"{infection_threshold}\n")
        f.write(f"{infectious_period}\n")
        for row in region:
            f.write(' '.join(row) + '\n')

def main():
    dimensions = int(input("Enter the dimensions of the region: "))
    total_population = int(input("enter total population: "))
    infectious_people = int(input("Enter number of infectious people: "))
    vaccinated_people = int(input("Enter number of vaccinated people: "))
    infection_threshold = int(input("Enter infection threshold: "))
    infectious_period = int(input("Enter infectious period: "))
    filename = input("Enter name of the input file: ")

    region = generate_region(dimensions, total_population, infectious_people, vaccinated_people)
    if region is not None:
        write_input_file(filename, region, infection_threshold, infectious_period)
        print(f"Input file {filename} has been generated successfully!")
    else:
        print("Failed to generate the input file.")


if __name__ == "__main__":
    from random import randint
    main()
