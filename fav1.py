import csv

with open("2018.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        best = row["rating"]
        if best in row:
            counts[best] += 1
        else:
            counts[best] = 1

for best in counts:
    print(f"{best}: {counts[best]}")
