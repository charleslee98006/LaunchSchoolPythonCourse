def CompoundInterests(initial_amount, years):
    balance = initial_amount;
    for i in range(0,years):
        balance = (balance*1.05)
        print(balance)

CompoundInterests(1000.00, 5)