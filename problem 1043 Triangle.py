A,B,C = map(float,input().split())
if (A+B)>C and (A+C)>B and (B+C)>A:
    perimeter = (A+B+C)
    print("Perimetro = %0.1f"%perimeter)
else:
    area = 0.5*(A+B)*C
    print("Area = %0.1f"%area)
