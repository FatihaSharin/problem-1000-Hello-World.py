n = int(input())

mul_two = 0
mul_three = 0
mul_for = 0
mul_five = 0

values= input().split()
values_cor = values[:n]
for i in range(n):
    values_cor[i] = int(values_cor[i])
    if(values_cor[i] % 2 == 0):
        mul_two += 1
    if(values_cor[i] % 3 == 0):
        mul_three += 1
    if(values_cor[i] % 4 == 0):
        mul_for += 1
    if(values_cor[i] % 5 == 0):
        mul_five += 1

print('{} Multiplo(s) de 2'.format(mul_two))
print('{} Multiplo(s) de 3'.format(mul_three))     
print('{} Multiplo(s) de 4'.format(mul_for))     
print('{} Multiplo(s) de 5'.format(mul_five))
