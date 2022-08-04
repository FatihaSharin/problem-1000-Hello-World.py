while (True):
    try:
        v = float(input())
        d = float(input())
        r = d / 2
        area = 3.14 * r * r
        alt_a = v / (r * r * 3.14)
        print("ALTURA = %0.2f"%alt_a)
        print("AREA = %0.2f"%area)
        
    except EOFError:
        break
