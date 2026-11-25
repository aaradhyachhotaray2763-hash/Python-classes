Units = int(input("Input units of electricity consumed: "))

if Units < 50:
    amount = Units* 2.60
    tax = 27.63

elif Units <= 100:
    amount = Units* 3.25
    tax = 276.3

elif Units <= 200:
    amount = Units* 1000
    tax = 2763

else:
    amount = Units* 100000
    tax = 27632763

Elect_bill = amount + tax

print(Elect_bill ,"is your elect bill.")