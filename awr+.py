text = "Testy!\n"

with open("new_file.txt", "r") as r:
    print(r.readline())
    print(r.readline())
    print(r.readline())

# with open("myfile.txt", "a") as r:
#     r.write("\nTifa")

# with open("new_file.txt", "w") as r:
#     r.write("All this in a brand new file  \nNext line  \nThe next line")


with open("myfile.txt", "r") as f:
   # for line in f:
   #     print(line)
    f1 = f.read(10)
    print(f1)

    f1 = f.read(10)
    print(f1)

    f1 = f.read(10)
    print(f1)