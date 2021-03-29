areaSize = int(input("Enter the size of the area:"))
nLiters = (areaSize/3)
nCansFloat = (nLiters/18)
nCansInt = 0
if (nCansFloat % 2) != 0:
    nCansInt = int(nCansFloat)+1
price = (nCansInt*80)

print("You will use approximately %.2f liters of paint in your work, we suggest that you buy %d cans of paint, in which you will spend R$ %d" %
      (nLiters, nCansInt, price))
