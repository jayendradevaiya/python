def calculate_bill(cups,price_per_cost):
    return cups * price_per_cost

my_bill = calculate_bill(3,15)

print(my_bill)

print("Order for table 2: ", calculate_bill(2,50))