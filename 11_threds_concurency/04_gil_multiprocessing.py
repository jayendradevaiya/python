from multiprocessing import Process
import time

def crunch_nummber():
    print(f"Started the count process...")
    count=0
    for _ in range(100_000_000):
        count+=1
    print(f"Ended the count process...")

if __name__ =="__main__":
    start = time.time()

    p1 = Process(target=crunch_nummber)
    p2 = Process(target=crunch_nummber)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"total taken:{end-start:.2f} sconds")

