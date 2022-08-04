while True:
    try:
        l = int(input())
        v = input().split()
        a= 0
        for i in range(l):
            if int(v[i]) > a:
                a = int(v[i])

        if a < 10:
            b = 1
        elif a >= 10 and a < 20:
            b = 2
        else:
            b = 3
        print(b)

    except EOFError:
        break
