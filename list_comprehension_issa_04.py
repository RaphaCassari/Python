#by: Rapha_Cassari
number = int(input("Enter an integer:"))
pairNumbers = []
for n in range(number+1):
    if ((n*n) % 2) == 0:
        pairNumbers.append(n*n)
    n = n+1
print(pairNumbers)
