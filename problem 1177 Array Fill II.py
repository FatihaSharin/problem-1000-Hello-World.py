n = int(input())
temp = 0
for i in range(1000):
    print("N[%d] = %d" %(i, temp))
    temp += 1
    if (temp == n):
        temp = 0
