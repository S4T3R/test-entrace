from math import *
a = int(input("what is the value of a: "))
b = int(input("what is the value of b: "))
c = int(input("what is the value of c: "))
print("this is the problem: ")
def quadro(a, b, c):
    if a == 1:
        print("x^2", "+", str(b) + "x", "+", str(c), "= 0")
    else:
        print(str(a) + "x^2", "+", str(b) + "x", "+", str(c), "= 0")

    d = b**2 - 4*a*c
    if d < 0:
        print("vo nghiem")
    elif d == 0:
        x = -b/(2*a)
        print("nhiem phuong trinh la: ", x)
    elif d > 0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print("nhiem phuong trinh la: ", x1, ",", x2)

quadro(a, b, c)