import csv

with open('data/output.csv', 'w') as f:
    quoting = csv.QUOTE_ALL
    writer = csv.writer(f, quoting=quoting)
    writer.writerow(([1, 2, 3, 4]))
