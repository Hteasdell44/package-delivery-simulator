# Student ID: 011646683

import csv
import datetime
from models.truck import Truck
from builtins import ValueError
from hash_table import HashTable
from models.package import Package

# Helper Functions

# Loads the hash table with package data from the csv file.
def load_hash_table(filename, hash_table):

    # Open the CSV file and read package data
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        
        # Iterate through each row in the CSV data
        for package in package_data:
            # Extract package information
            packageID = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            weight = package[6]
            status = "At The Hub!"

            # Create Package object with loaded package data and insert it into the hash table
            package_data_object = Package(packageID, address, city, state, zip_code, deadline, weight, status)
            hash_table.insert(packageID, package_data_object)


# Nearest neighbor algorithm implementation to find an optimal delivery route.
def find_optimal_route(truck):

    # List to store packages that need to be delivered.
    packages_to_deliver = []

    # Populate the packages_to_deliver list with all package objects in the truck's packages attribute.
    for packageID in truck.packages:
        package = hash_table.lookup(packageID)
        packages_to_deliver.append(package)

    # Clear the truck's packages so that they can be re-added in an optimal order.
    truck.packages = []


    while len(packages_to_deliver) > 0:

        # Initialize variables for the next nearest package and its address.
        next_address = float('inf')  # Set to positive infinity initially.
        next_package = None

        # Iterate through the remaining packages to find the nearest one.
        for package in packages_to_deliver:
            # Calculate the distance from the current truck location to the package address.
            distance_to_package = calculate_distance(extract_address(truck.address),extract_address(package.address))

            # Check if the current package is closer than the previously found nearest package.
            if distance_to_package <= next_address:
                next_address = distance_to_package
                next_package = package

        # Update truck and package information for the nearest package
        truck.packages.append(next_package.ID)
        packages_to_deliver.remove(next_package)
        truck.mileage += next_address
        truck.address = next_package.address
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time

# Calculate the distance between two addresses.
def calculate_distance(x, y):
    distance = csv_distance[x][y]

    # If the distance is not available in one direction, use the distance from the opposite direction
    if distance == '':
        distance = csv_distance[y][x]

    return float(distance)

 # Extract address information from CSV data
def extract_address(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])

# Main program function
def main():
    # Establishing necessary variables and making them accessible throughout the program
    global csv_distance, csv_address, csv_package, hash_table, truck_one, truck_two, truck_three

    # Load CSV data and initialize
    csv_distance = list(csv.reader(open("csv/distance_data.csv")))
    csv_address = list(csv.reader(open("csv/address_data.csv")))
    csv_package = list(csv.reader(open("csv/package_data.csv")))

    # Initialize hash table
    hash_table = HashTable()
    
    # Load package data into the hash table
    load_hash_table("csv/package_data.csv", hash_table)

    # Initialize the three delivery trucks based on special notes
    truck_one = Truck(1, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], datetime.timedelta(hours=8))
    truck_two = Truck(2, [3, 6, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], datetime.timedelta(hours=9, minutes=5))
    truck_three = Truck(3, [2, 4, 5, 7, 8, 9, 10, 11, 12, 25, 28, 32, 33], datetime.timedelta(hours=10, minutes=20))

    # Use the nearest neighbor implementation to find the optimal delivery route for each truck
    find_optimal_route(truck_one)
    find_optimal_route(truck_two)
    
    # There are only two drivers, so Truck three cannot leave before one of the drivers returns. 
    # Thus, the departure time is set for truck three based on the minimum time of truck one and two.

    truck_three.depart_time = min(truck_one.time, truck_two.time)
    find_optimal_route(truck_three)

    

    # Displaying user interface in command line.

    # Display a welcome message
    print("\n\033[1mWelcome To The Western Governors University Parcel Service Dashboard!\033[0m")

    while True:

        # Resets the delivery address of the ninth package so that if someone searches for an earlier time after a later time, the address will adjust accordingly and persist the updated address. 
        hash_table.lookup(9).address = "300 State Street"

        # Display options to the user
        print("\nWould You Like To:\n")
        print("1. Check Package Status")
        print("2. View Today's Total Route Mileage")
        print("3. Quit")

        # Collect user input for desired action
        choice = input("\nEnter your choice (1, 2, or 3): ")

        # Check the user's choice and perform the corresponding actions
        if str(choice) in ["1", "status"]:
            try:
                print("\n\033[1mSelect a Time to View Package Status:\033[0m\n")
                print("1. 09:00:00")
                print("2. 10:00:00")
                print("3. 13:00:00")
                print("4. Enter Custom Time")

                # Collect user input for desired action
                time_choice = input("\nEnter your choice (1, 2, 3, or 4): ")

                # Check the user's choice and perform the corresponding actions
                if str(time_choice) == "1":
                    user_time = "09:00:00"

                elif str(time_choice) == "2":
                    user_time = "10:00:00"

                elif str(time_choice) == "3":
                    user_time = "13:00:00"

                elif str(time_choice) == "4":
                    user_time = input("\n\033[1mPlease enter a time to view package status (Ex: '13:15:00'). Use military time format 'HH:MM:SS' with quotation marks:\033[0m\n\n")

                else:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")
                    continue

                # Convert the user-entered time to a timedelta object
                convert_timedelta = datetime.timedelta(hours=int(user_time[:2]), minutes=int(user_time[3:5]), seconds=int(user_time[6:]))

                # Checks the time, updating the address of the package with id 9 after 10:20am in accordance with the updated customer address.
                if convert_timedelta >= datetime.timedelta(hours=10, minutes=20):
                    hash_table.lookup(9).address = "410 S State Street"

                # Display options to the user 
                print("\nWould You Like To View:\n")
                print("1. An Individual Package")
                print("2. All Packages")

                # Collect user input for desired action
                second_input = input("\nEnter your choice (1 or 2): ")

                # Check the user's choice and perform the corresponding actions
                if str(second_input) == "1":
                    try:
                        solo_input = input("Enter the package ID: ")
                        package = hash_table.lookup(int(solo_input))
                        package.update_status(convert_timedelta)
                        print(str(package))

                    # Invalid input
                    except ValueError:
                        print("Invalid package ID. Please enter a numeric value.")

                elif str(second_input) == "2":
                    try:
                         # Loop through all package IDs and display their status
                        for packageID in range(1, 41):
                            package = hash_table.lookup(packageID)
                            package.update_status(convert_timedelta)
                            print(str(package))

                    # Invalid input  
                    except ValueError:
                        print("Invalid package ID. Please enter a numeric value.")

                # Invalid input
                else:
                    print("Invalid input. Please enter '1' or '2'.")

            # Invalid input
            except ValueError:
                print("Invalid time format. Please use military time format 'HH:MM:SS' (Ex: '13:15:00'):")

        elif str(choice) == "2":
            # Display total route mileage between all three trucks.
            print("\n\033[1mToday's total route mileage is: {} miles\033[0m".format(truck_one.mileage + truck_two.mileage + truck_three.mileage))

        elif str(choice) == "3":
            # Exit program
            print("\n\033[1mExiting program. Thanks For Using The Western Governors University Parcel Service Dashboard!\033[0m\n")
            exit()

        # Invalid input
        else:
            print("Invalid input. Please enter '1', '2', or '3'.")

# Call the main function.
main()
