import csv
import json

with open("data/example1.csv", "r") as file:
    reader = csv.reader(file)
    # print(reader.dialect.delimiter)
    # print(reader.dialect.quoting)
    # print(reader.dialect.lineterminator)
    # print(reader.line_num)
    for row in reader:
        if reader.line_num == 2:
            obj = row[1]
            print(obj)
            dct = json.loads(obj)
            print(dct.get('cat'))
        print(reader.line_num, row)
