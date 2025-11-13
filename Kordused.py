#1
while True:
    try:
        w = int(input("int n = "))
        if w > 9:
            print("Vale number!")
        elif w < 0:
            print("Vale number!")
        else:
            break
    except:
        print("Vale andmpetüüp!")
for n in range (w):
                print("""    /V\    
   / V \ 
  / V V \  
 /VV V VV\    """)
                print(" ")

#2
import math
while True:
        try:
            R = int(input("int R = "))
            if R <= 0:
                print("Vale number!")
            else:
                break
        except:
            print("Vale andmetüüp!")
r = 1
m = 1
o = R + 1
for i in range(o):
    if r <= R:            
       m *= r
       r = r + 2
print(f"Result on {m}")
print(" ")
#3
import random
N = random.randint(1, 1000)
pos = 0
for i in range (N):

    p = random.randint(-999, 999)
    if p > 0:
       pos += 1
print(f"random pos: {pos}")
print(" ")
#4
while True:
        try:
            nat=int(input("int num = "))
            break
        except:
            print("Vale andmetüüp!")
even = 0
odd = 0
for i in str(nat):
    if int(i)%2 == 0:
        even += 1
    else:
        odd += 1
print(f"Odd = {odd}")
print(f"Even = {even}")
print(" ")
            
#5
while True:
     try:
            A=int(input("int A = "))
            B=int(input("int B = "))
            break
     except:
            print("Vale andmetüüp!")
if A < B:
    num = A
    loop = B - A
    summ = A
    for i in range(loop):
        if num <= B:           
           A += 1
           summ += A
           num += 1
        else:
           print(f"Summa on {summ}")
elif A > B:
    num = B
    loop = A - B 
    summ = B
    for i in range(loop):
        if num <= A:
            B += 1
            summ += B
            num += 1
        else:
            print(f"Summa on {summ}")
else:
    print("Vale numbrid!")
