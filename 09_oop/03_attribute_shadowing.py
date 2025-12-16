class Chai:
    temperature = "hot"
    strength = "Strong"
    cup ="big"


cutting = Chai()
print(cutting.temperature)

cutting.temperature= "mild"
cutting.cup = "small"
print("After changing ", cutting.temperature)
print("cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature 
del cutting.cup 
print(cutting.temperature)
print(cutting.cup)