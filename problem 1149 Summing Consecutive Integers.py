list1 = list(map(int, input().split()))
n1 = 'I'
n2 = 0
sum1= 0
for i in list1:
    if (n1 == 'I'):
        n1= i
    else:
        if (i > 0):
            n2 = i
            break

for i in range(n2):
    sum1 += n1
    n1 += 1

print("%d"%sum1)
