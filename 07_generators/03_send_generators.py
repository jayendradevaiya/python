def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start generator execution

stall.send("Masala Chai")
stall.send(input("order your tea type:"))