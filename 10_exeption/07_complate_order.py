class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala":20, "ginger":40} 
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not avalable")
        if not isinstance(cups, int):
            raise TypeError("Numer of cups must be an integer")
        total = menu[flavor] * cups
        print(f"your bill for {cups} cups of {flavor} chai : rupees {total}")
    except Exception as e:
        print("Error :", e)
    finally:
        print("Thank you for visiting us!")

bill("mint",2)
bill("masala","three")
bill("ginger",4)