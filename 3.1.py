from token import MINUS
from venv import create


#k = 0
#for i in range(15):
 #   while True:
  #      try:
   #         arv = float(input(f"Sisesta {i+1}. arv: "))
    #        break
     #   except:
      #      print("Vale andmetüüp!")
   # if int(arv)==arv:
   #     print(f"{arv} on täisarv")
   #     k+=1

#print(f"{k} on täisarv")

#2

s = 0
while True:
    try:
        a=int(input("Number a on: "))
        break
    except:
        print("Vale andmetüüp!")
for i in range(1, a+1):
       s=s+i
print(f"Summa vahemikus 1 kuni {a} vordub {s}")
 
#3
for i in range(8):
    while True:
        try:
            mult= float(input(f"Sisesta {i+1}. arv: "))
            break
        except: 
            print("Vale andmetüüp!")
    
#4
korrutis = 1
while True:
    try:
        arv=int(input("Number on: "))
        if arv > 0: break
    except:
        print("Vale andmetüüp!")
    korrutis *= arv
print(f"Korrutis võrdub {korrutis}")

#4
for i in range(10, 20):
    print(f"Arv {i} ruut on {i**2}")

#5
for i in range(N):
    while True:
        try:
            N=int(input("Numbrid on: "))
            arv=float(input("Number on: "))
            break
        except:
            print("Vale andmetüüp!")
    for i in range(N):
        if int(arv) >= 0:
            int(arv) == 0
        else:
            int(arv) == int(arv)
        print(f"arv on ")

#6

for i in range(N):
    while True:
        try:
            N=int(input("Numbrid on: "))
            arv=float(input("Number on: "))
            break
        except:
            print("Vale andmetüüp!")
        if int(arv) > 0:
            int(arv) = pluus
        elif int(arv) < 0:
            int(arv) = minuss
        else:
            int(arv) = null

#7
for i in range(A, B):
    while True:
        try:
            A=int(input("A on: "))
            B=int(input("B on: "))
            break
        except:
            print("Vale andmetüüp!")
