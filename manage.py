# fibonacci  1=1=2 2+1=3 3+2=5 5+3=8 8+5=13 13+8=21 21+13=34
# 1,1,2,3,5,8,13,21,34


try:
    x = 10 / 0
except ZeroDivisionError:  # except Exception:
    print("division by zero")
else:
    print(int(x))
finally:
    print("Done")
