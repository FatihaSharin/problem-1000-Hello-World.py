n = int(input())
x = input().split()

for i in range(n):
    x[i] = int(x[i])

minimum = min(x)
result = x.index(minimum) + 1

print(result)
