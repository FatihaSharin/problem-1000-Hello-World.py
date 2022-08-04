def variable():
    x= float(input())
    return x

def impress(number):
    count = 0
    if number >= 1 and number < 10:
        print('+{:.4f}E+00'.format(number))
    elif number > 0 and number < 1:
        while number < 1:
            count += 1
            number *= 10
        if count < 10:
            print('+{:.4f}E-0{}'.format(number,count))
        else:
            print('+{:.4f}E-{}'.format(number,count))
    elif number >= 10:
        while number >= 10:
            count += 1
            number /= 10
        if count < 10:
            print('+{:.4f}E+0{}'.format(number,count))
        else:
            print('+{:.4f}E+{}'.format(number,count))
    elif number < -1 and number > -10:
        print('-{:.4f}E+00'.format(abs(number)))
    elif number < 0 and number > -1:
        number = abs(number)
        while number < 1:
            count += 1
            number *= 10
        if count < 10:
            print('-{:.4f}E-0{}'.format(number,count))
        else:
            print('-{:.4f}E-{}'.format(number,count))
    elif number <= -10:
        number= abs(number)
        while number >= 10:
            count += 1
            number /= 10
        if count < 10:
            print('-{:.4f}E+0{}'.format(number,count))
        else:
            print('-{:.4f}E+{}'.format(number,count))
    elif number == 0.0:
        if str(number)[0] == '-':
            print('{:.4f}E+00'.format(number))
        else:
            print('+{:.4f}E+00'.format(number))


impress(variable())
