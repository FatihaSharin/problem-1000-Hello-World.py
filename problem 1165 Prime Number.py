n = int(input())

for i in range(n):
    a = int(input())
    b = 0
    for j in range(1, a + 1):
        if(a % j == 0):
            b = b + 1
    if(b == 2):
        print("{} eh primo".format(a))
    else:
        print("{} nao eh primo".format(a))
