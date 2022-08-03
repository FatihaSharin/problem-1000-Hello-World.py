a = []
for i in range(20):    
    value = int(input())
    a.append(value)
pos = 0
for l in a[::-1]:
    print("N[%d] = %d" %(pos, l))
    pos += 1
