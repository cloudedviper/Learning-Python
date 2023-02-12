# x = [1, 2, 3, 4, 5, 6, 7]
list1 = []


# list1 = [x**3 for x in range(10)]
# print(list1)

def list2():
    for i in range(10):
        list1.append(i ** 3)


# arg and kwargs

# def mysum(a, b, c):
#      print(a+b+c)
#
mylist = [0, 1, 2]
# mysum(*mylist)


# enumerate    (index, item)
for x, element in enumerate(mylist):
    print(x, element)
# seasons = ["spring", "summer", "fall", "winter"]
# for count, seasons in enumerate(seasons, start=1):
#     print(count, seasons)
