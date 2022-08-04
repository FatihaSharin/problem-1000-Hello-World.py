a, b = input().split(' ')
a = float(a)
b = float(b)

price = b * 100
result = price / a
print('{:.2f}%'.format(result - 100))
