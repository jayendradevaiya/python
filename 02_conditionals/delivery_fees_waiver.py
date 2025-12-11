order_amount = int(input("Enter your order amount heare:"))

# if order_amount > 300 :
#     print(f"your delivery is free")
# else:
#     print(f"your delivery fee is $30 rupees")

delivery_fees = 0 if order_amount > 300 else 30

print(f"delevery fees is : {delivery_fees}")