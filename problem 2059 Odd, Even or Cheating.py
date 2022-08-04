p, p1, p2, r, a = input().split()

result = (int(p1) + int(p2)) % 2

if((r == "1") and (a == "1")):
    print("Jogador 2 ganha!")

elif((r == "1") or (a == "1")):
    print("Jogador 1 ganha!")

else:
    if(result == 0):
        if(p == "1"):
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    elif(result == int(p)):
        print("Jogador 2 ganha!")
    else:
        print("Jogador 1 ganha!")
