a = int(input())
while a >= 1:
    b = int(input())
    if(b < 2015):
        year = 2015 - b
        print("%d D.C." %year)
    else:
        year= b-2014
        print("%d A.C." %year)
    a = a - 1
