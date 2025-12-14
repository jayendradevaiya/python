
def infinte_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

rerill = infinte_chai()
user2 = infinte_chai()

for _ in range(10):
    print(next(rerill))

for _ in range(6):
    print(next(user2))
