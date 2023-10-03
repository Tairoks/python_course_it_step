import csv

sniffer = csv.Sniffer()

with open('test_data.csv', 'r') as file:
    example = file.readline()
    dialect = sniffer.sniff(example)

    reader = csv.DictReader(file, fieldnames=example.strip().split(';'), dialect=dialect)
    data = [row for row in reader]

with open('test_data_reformat.csv', 'w') as output:
    writer = csv.DictWriter(output, fieldnames=example.strip().split(';'), lineterminator='\n')
    writer.writeheader()

    for row in data:
        writer.writerow(row)


# with open('test_data.csv', 'r') as file:
#     data = []
#     reader = csv.reader(file)
#     for row in reader:
#         if reader.line_num == 1:
#             fields = row[0].split(';')
#             continue
#         else:
#             data.append(row[0].split(';'))
#     # print(data)
#
# with open('test_data_reformat.csv', 'w') as output:
#     writer = csv.DictWriter(output, fieldnames=example.strip().split(';'), lineterminator='\n')
#     writer.writeheader()
#
#     for elem in data:
#         writer.writerow({
#             "id": elem[0],
#             "Length": elem[1],
#             "Dose": elem[2],
#             "Term": elem[3],
#             "Category": elem[4]
#         })

