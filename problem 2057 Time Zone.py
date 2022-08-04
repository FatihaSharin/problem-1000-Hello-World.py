s, t, f = map(int,input().split())
if s == 0:
    s = 24
chegada = s + t + f
if chegada > 24:
    chegada = chegada - 24
    print(chegada)
elif chegada == 24:
    chegada = 0
    print(chegada)
else:
    print(chegada)
