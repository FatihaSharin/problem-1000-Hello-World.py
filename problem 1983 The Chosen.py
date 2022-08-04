n = int(input())
m = 0.0
o = 0
while(n > 0):
    n -= 1
    a, b = input().split()
    if float(b) > m:
        m = float(b)
        o = int(a)
        
if m >= 8:
    print(o)
else:
    print("Minimum note not reached")
