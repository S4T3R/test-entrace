a = [1, 2, 4, 7]

print("this is my sequence: ")
print(*a)

print("what you wanna remove(head or tail): ")


b = (input())
if b == "head":
    a.pop(0)
    print(a)
elif b == "tail":
    c = len(a) - 1
    a.pop(c)
    print(a)
