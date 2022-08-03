list_a = [0, 1, 1]

r = "0, 1, 1"
ant = 1
actual = 1
value = int(input())

for v in range(value - 3):
    t = actual
    actual += ant
    ant = t
    lista.append(actual)

print(str(list_a[0 : value]).replace(",", "").replace("[", "").replace("]", ""))
