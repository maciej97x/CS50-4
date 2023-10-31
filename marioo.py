while True:
    n = int(input("Height: "))
    if n > 0 and n < 99:
        break

for i in range(0, n, 1):
    for j in range (0, n+i+2, 1):
        if (j == n or i+j < n-1):
            print(" ", end="")
        else:
            print("#", end="")
    print()