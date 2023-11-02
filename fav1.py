import csv

with open("2018.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        best = row["team"]
        if best in row:
            counts[best] += 1
        else:
            counts[best] = 1
def get_value(team):
    return counts[team]

for best in counts:
    print(f"{best}: {counts[best]}")
