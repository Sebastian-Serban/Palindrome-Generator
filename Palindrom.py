a = int(input("a = "))
b = int(input("b = "))
for i in range(a, b + 1):
    o = str(i)
    r = o[:: -1]
    if (o == r):
        print(o)
        
