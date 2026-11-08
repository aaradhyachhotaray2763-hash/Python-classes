actual_amount = float(input("Enter product's actual price: "))
sale_amount = float(input("Enter product's sold price: "))

if sale_amount > actual_amount:
    profit = sale_amount - actual_amount
    print("This is your profit amount: {0}". format(profit))

else:
    print("Unfortunately you haven't been able to get a profit.")