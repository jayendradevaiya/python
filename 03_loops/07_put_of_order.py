flavours = ["Ginger","Out of Stoke","Lemon","Discontinued","Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stoke":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")
print("Out side of loop")