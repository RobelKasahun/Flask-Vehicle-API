import csv


def read_csv():
    vehicles = []
    file_name = "./data/vehicles.csv"
    # open and read data from the csv file
    with open(file_name) as file:
        reader = csv.DictReader(file)
        # read each row of the csv file as a dictionary
        for row in reader:
            vehicles.append(row)

    return vehicles
