import sys

names = {"Maciej", "Kuba"}

name = input("Name: ")

for n in names:
    if name == n:
        print("Found")
        sys.exit(0)

print("Not found")
sys.exit(1)