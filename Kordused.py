#1
w = int(input("n = "))
if w > 9:
    print("Vale")
elif w < 0:
    print("Vale")
else:
    for n in range (w):
        while True:
            try:
                print("""\   /V\    
   / V \ 
  / V V \  
 /VV V VV\    """)
                print(" ")
                break
            except:
                print("No")

#2
import math
R = int(input("R = "))
if R % 2 != 0:
    print("Vale nümber!")
else:
    r = 0
    m = 0
    o = R + 1
    for i in range(o):
        try:        
            if r <= R:
                r = r + 2
                m *= r
            else:
                print(f"Result on {m}")
                break
        except:
            print("No")
#3
import random
N = random.randint(1, 1000)
pos = 0
for i in range (N):
    while True:
        try:
            p = random.randint(-999, 999)
            if p < 0:
                pos == pos
            elif p == 0:
                pos == pos
            else:
                pos += 1
        finally:
            break
            print(f"{pos}")
#4
nat=int(input("num = "))
even = 0
odd = 0
for i in string(nat):
    if int(i)%2 == 0:
        even += 1
    else:
        odd += 1
print(f"Odd = {odd}")
print(f"Even = {even}")
            


#5
A=int(input("A = "))
B=int(input("B = "))
num = A
loop = B - A
summ = A
for i in range (loop):
    while True:
        try:
            if num <= B:
                 summ += A
                 A += 1
                 num += 1
            else:
                break
        except:
            print("No")
print(f"Summa on {summ}")