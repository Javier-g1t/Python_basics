import csv

with open("files\\data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)