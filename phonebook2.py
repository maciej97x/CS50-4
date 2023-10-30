import csv

file = open("phonebook.csv", "r")

name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file)
writer.writerow([name, number])

file.close()