import csv

with open("2018.csv", "r") as file:
    reader = csv.DictReader(file)
    counts{}
    for row in reader:
        print(row["rating"])