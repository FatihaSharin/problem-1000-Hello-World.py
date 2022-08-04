def verify(a, b, c):
    if abs(b - c) < a < (b + c):
        if abs(a - c) < b < (a + c):
            if abs(a - b) < c < (a + b):
                return True
    else:
        return False


def variable():
    a, b, c, d = map(int,input().split())
    return a, b, c, d


def final_result(a, b, c, d):
    if verify(a, b, c) or verify(a, b, d) or verify(a, c, d) or verify(b, c, d):
        print('S')
    else:
        print('N')


def main():
    a, b, c, d = variable()
    final_result(a, b, c, d)

main()
