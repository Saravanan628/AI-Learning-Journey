import csv
def read_csv(filename):
    with open(filename, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


# Calling the function
file_name = input("Enter CSV file name: ")
read_csv(file_name)
