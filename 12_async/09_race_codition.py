import threading

chai_stock = 0

def restlock():
    global chai_stock
    for _ in range(10000000):
        chai_stock +=1

threads = [threading.Thread(target=restlock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Chai stock: ",chai_stock)