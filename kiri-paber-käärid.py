import random
for i in range (3):
    while True:
        move = int(input("1 - paber, 2 - kiri, 3 - k‰‰rid. Move: "))
        if move < 1:
            print("Vale number!")
        elif move > 3:
            print("Vale number!")
        else:
            break
    win = 0
    comp = random.randint(1, 3)
    print("kivi... k‰‰rid... paber... ¸ks... kaks... kolm!")
    if comp == move:
        print("Viik")
    elif comp == 1 and move == 3:
        print("Win")
        win += 1
    elif comp == 1 and move == 2:
        print("Lose")
    elif comp == 2 and move == 3:
        print("Lose")
    elif comp == 2 and move == 1:
        print("Win")
        win += 1
    elif comp == 3 and move == 1:
        print("Lose")
    else:
        print ("Win")
        win += 1
if win >= 2:
    print ("Vaga tubli!")
else:
    print ("Ouu...")


