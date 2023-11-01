import csv

with open("2018.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(rating)