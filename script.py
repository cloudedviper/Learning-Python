if __name__ == "__main__":
    print("Executed when direct")
else:
    print("Executed when imported")

print(__name__)

# walrus :=
# happy = True
# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append((food))


foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
