s = input("Do you agree? ")

l = s.lower()
if l in ["Y", "y", "a"]:
    print("Agreed.")
elif l in ["N","n", "b"]:
    print("Not agreed.")
else:
    print("Null")
