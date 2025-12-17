import threading
import time
def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk Boiled...")

def tost_bun():
    print(f"Tosting bun...")
    time.sleep(2)
    print(f"Bun tosted...")
start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=tost_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"total taken:{end-start:.2f} sconds")