a = int(input())

while(a > 0):
    n = int(input())
    vector = []

    for i in range(n):
        if i % 2 == 0:
            vector.append(1)
        else:
            vector.append(-1)

    print(sum(vector))
    a -= 1
