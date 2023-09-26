import csv

with open('data/example1.csv', 'r') as f:

    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["category"])
    # list_of_devices = [row for row in reader]
    # print(list_of_devices)
