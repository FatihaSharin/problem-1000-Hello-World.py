x = int(input())
z = int(input())

a = 0
b = 1

while x >= z:
    z = int(input())
    
for i in range(x, z):
    a += i
    if a > z:
        break
    b += 1
print(b)
