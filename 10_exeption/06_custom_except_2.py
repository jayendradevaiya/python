class OutofIngredientsError(Exception):
    pass

def make_chai(milk, suger):
    if milk == 0 or suger == 0:
        raise OutofIngredientsError("Missing milk or suger")
    print("chai is ready ...")

make_chai(0,1)