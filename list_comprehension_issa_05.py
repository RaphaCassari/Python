number = int(input("Enter an integer:"))
for n in range(1, number+1):
    for n2 in range(n):
        print(n, end='  ')
    print()
