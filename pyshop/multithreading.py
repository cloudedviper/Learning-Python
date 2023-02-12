# multithreading
# gil lock = (global interpreter lock)
# allows only 1 thread to hold control of python interpreter at 1 time

import threading
import time


def new():
    for i in range(1000):
        print("Thread1")


def new2():
    for i in range(1000):
        print("thread2")


def new3():
    for i in range(1000):
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

# class multithreading

# class Mythread(threading.Thread):
#     def run(self):
#         for x in range(10):
#             print("thread")
#
# obj = Mythread()
# obj.start()
# obj.join()

mylist = [0, 1, 2]
thislist = [1, 2, 3, 4, 5, 6, 7]
seasons = ["spring", "summer", "fall", "winter"]
# enumerate    index, object
for x, element in enumerate(seasons):
    print(x, element)
    # if x == 1:
    #     print("1")
# for count, seasons in enumerate(seasons, start=1):
#     print(count, seasons)
