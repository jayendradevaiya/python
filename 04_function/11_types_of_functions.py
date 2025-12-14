def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups

def pore_chai(n):
    if n==0:
        return "All cups poured"
    return pore_chai(n-1)

print(pore_chai(5))

chai_type = ["light","kadak","ginger","kadak"]

strong_chai = list(filter(lambda chai:chai=="kadak",chai_type))

print(strong_chai)