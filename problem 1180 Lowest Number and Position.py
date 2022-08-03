n = int(input())
list1 = list(map(int, input().split()))
b = 0
c = list1[0]
count = 0
for i in list1:
    if (i < c):
        c = i
        b = count
    count += 1
print("Menor valor: %d" % c)
print("Posicao: %d" % b)
