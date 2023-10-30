print('Let build a Mario pyramid! Buy how high? Give me a positive int between 1 and 24: ', end='')
while True:
    height = int(input())
    if height < 1 or height > 24:
        print('Nah! Give me an int between 1 and 24!')
    else:
        break

# print the pyramid (semi-readable one liner)
for row in range(height+1):
    print(' ' * (height - row) + '#' * row + '  ' + '#' * row)