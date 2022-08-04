def DH(n):
    DHNum = ['0'] * 100
    i = 0
    while (n != 0):
        temp = 0
        temp = n % 16
        if (temp < 10):
            DHNum[i] = chr(temp + 48)
            i = i + 1
        else:
            DHNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
    j = i - 1
    while (j >= 0):
        print((DHNum[j]), end="")
        j = j - 1
n = int(input())
DH(n)
print()
