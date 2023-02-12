# __iter__()   __next__()   iterators
# yield   Generator

# mytuple = (1, 2, 3, 4, 5)
# myiter = (next(mytuple))

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

mytuple = ("Cloud", "Tifa", "Yuffie")
# myiter = iter(mytuple)
loop = mytuple.__iter__()
print(loop.__next__())
print(loop.__next__())

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# for i in mytuple:
#     print(i)
#
# def subjects():
#     yield "Cloud"
#     yield "Tifa"
#     yield "Yuffie"
#     yield "Barret"
#
#
# for i in subjects():
#     print(i)

# i = subjects()
# print(next(i))
# print(next(i))
# print(next(i))


