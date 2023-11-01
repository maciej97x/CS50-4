import csv

with open("2018.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])