while (True):
    try:
        x,y = map(int,input().split())
        
        if x == y:
            break
        else:
            if x < y:
                print("Crescente")
            elif x > y:
                print("Decrescente")
                
    except EOFError:
        break
