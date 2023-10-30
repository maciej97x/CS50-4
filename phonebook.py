people = {
    "Maciej": "382 319 293",
    "Kuba": "932 012 832"
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")