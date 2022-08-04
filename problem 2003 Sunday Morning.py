while True:
    try:
        h = input().split(':')
        n = int(h[0]) * 60 + int(h[1]) - 420
        if n < 0:
            n = 0
        print("Atraso maximo: %d"%n)
        
    except EOFError:
        break
