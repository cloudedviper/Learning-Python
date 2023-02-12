# gil lock = (global interpreter lock)
# allows only 1 thread to hold control of python interpreter at 1 time

import threading
import time


def new():
    for i in range(10000):
        print("Thread1")


def new2():
    for i in range(11000):
        print("thread2")


def new3():
    for i in range(21000):
        print("thread3")


t1 = threading.Thread(target=new)
t1.start()
t2 = threading.Thread(target=new2)
t2.start()
t3 = threading.Thread(target=new3)
t3.start()

t1.join()
t2.join()
t3.join()

print(threading.enumerate())
print(threading.active_count())
print(time.perf_counter())