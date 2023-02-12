# lambda
# lambda 0 or more argument(s) : expression(s)   is return value

# (lambda x : 2*x)(2)
#
# z = lambda x, y : x*y

# map()    map(function, list of iterables)
if __name__ == "__main__":
    print("running this module directly")
else:
    print("Indirectly")

print(__name__)
z = ["cloud", "tifa", "yuffie", "sephiroth"]
y = []

for i in z:
    y.append(z)
print(y)

#print(list(map(lambda x : x, z)))

#filter   filter()   filter(function, 1 iterable)

