def variable():
    n, l = map(int,input().split())
    return n, l

def perimeter(n, lado):
    return n * lado

def main():
    n, l = variable()
    print(perimeter(n, l))

main()
