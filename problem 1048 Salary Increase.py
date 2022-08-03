sal= float(input())

if (sal >= 0 and sal <= 400.00):
    n_sal = sal * 0.15
    in_sal = sal + n_sal
    per= 15
elif (sal >= 400.01 and sal <= 800.00):
    n_sal = sal * 0.12
    in_sal = sal + n_sal
    per = 12
    
elif (sal >= 800.01 and sal <= 1200.00):
    n_sal = sal * 0.10
    in_sal = sal + n_sal
    per = 10

elif (sal >= 1200.01 and sal <= 2000.00):
    n_sal = sal * 0.07
    in_sal = sal + n_sal
    per = 7
    
elif (sal > 2000):
    n_sal = sal * 0.04
    in_sal = sal + n_sal
    per = 4
    
    
print("Novo salario: %0.2f"%in_sal)
print("Reajuste ganho: %0.2f"%n_sal)
print("Em percentual: {} %".format(per))
