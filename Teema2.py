
#1. Juku
#a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
#b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)
#  <6 aastad  - tasuta
# 6-14 - lastepilet
#15-65 - täispilet
#>65 - sooduspilet
#<0 ja >100 viga andmetega


eesnimi=input("Sisesta eesnimi: ")
if eesnimi=="Juku":
    print("Lähme Jukuga kinno!")
    vanus=input("Sisesta Juku vanus: ")
    if vanus.isdigit():
        vanus=int(vanus)
        if vanus<0 or vanus>100:
             print("Viga andmetega!")
        elif vanus<6:
             print("Pilet on tasuta!")
        elif vanus <=14:
             print("Lastepilet")
        elif vanus<=65:
             print ("Täistpilet")
        else:
             print ("Sooduspilet")
    else:
            print("Palun sisesta vanus täisarvuna!")

#2 Pinginaabrid

#Küsi kahe inimese nimed. Kui nimed koosnevad ainult tähedest siis  teavita kasutajat, kas nad on täna pinginaabrid või ei mitte.
nimi1 = input("Sisesta nimi => ").capitalize()
nimi2 = input("Sisesta nimi => ").capitalize()
if nimi1.isalpha() and nimi2.isalpha(): 
    if nimi1=="Kostya" and nimi2=="Kiriil" or nimi1=="Kiril" and nimi2=="Kostya":
        print(f"{nimi1} ja {nimi2} on täna pinginaabrid")
    else:
        print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
else:
    print("Palun sisesta ainult tähed")

#3
pikkus = int(input('Sisestage pikkus: '))
laius = int(input('Sisestage laius: '))
if pikkus> 0 and laius>0:
    pindala = pikkus * laius

    print(f'pindala suurus on  {pindala}')
    user = input('Kas soovite remondi teha? ').capitalize()
    if user.isalpha() and user == 'Jah':
        hind = float(input('Ruut meetri hind => '))
        if hind>0:
            remondi_hind = hind * pindala
            print(f'Remondi summa on {remondi_hind} euro')
            kes = input('Kes teeb remondi? (ise/töötaja)? ').capitalize()
            if kes.isalpha() and kes =="Ise":
                print(f"Siis suuma {remondi_hind}")
            elif kes=="Töötaja":
                print(f"Siis suuma {remondi_hind + 300}")
        else:
            print("Hind ei sa olla negatiivne!")
    else:
        print('Head aega!')
else:
    print ("Arvud  paevad olema suurem kui 0")

#4

from curses.ascii import isdigit
hind = input ("Hind: ")

if hind.isdigit():
    hind = float(hind)
    if hind > 700:
        hind *= 0.7
        print(f"Soodus hind võrdub {hind}")
    else:
        print("Hind on väike")

#5

try:
    t=float(input("Sisesta temperatuur:"))
    if t>18:
        print("Soovitatav toasoojus talvel")
    else:
        print("Võib olla jahe")
except:
    print("Palun sisesta temperatuur ujukomaarvuna")

#6

pikk=float(input("Pikk on "))
if pikk<5:
    print("Pikk on lühike")
elif 5<pikk<6:
    print("Pikk on keskmine")
elif pikk>6:
    print("Pikk on pikk")
else:
    print("Pikk on ???")

#7

pikk2=float(input("Pikk on "))
sugu=input("Sugu on ").capitalize()
if pikk2<5:
    print("Pikk on lühike")
elif 5<pikk2<6:
    print("Pikk on keskmine")
elif pikk2>6:
    print("Pikk on pikk")
else:
    print("Pikk on ???")
if sugu=="Mees":
    print (f"Sugu on {sugu}")
elif sugu=="Naine":
    print(f"Sugu on {sugu}")
else:
    print("Sugu on ???")

#8

import math
import random

item=input("Mis te on soovite? ").capitalize()
leib==random.randint(1.2, 3.5)
piim==random.randint(0.4, 1.3)
if item=="Piim":
    print(f"Piim on {piim} euro")
elif item=="Leib":
    print(f"Leib on {leib} euro")
else:
    print("?")

#9

hor=float(input("Mis on a? "))
vert=float(input("Mis on b? "))
if a==b:
    print("See on ruut")
else:
    print("See ei ole ruut")

#10

number1=float(input("Mis on number1? "))
number2=float(input("Mis on number2? "))
Operatsioon=input("Mis on operatsioon sümbol? ").capitalize()
if Operatsioon == "+":
    number3 == number1 + number2
    print(f"{number3}")
elif Operatsioon == "-":
    number3 == number1 - number2
    print(f"{number3}")
elif Operatsioon == "*":
    number3 == number1 * number2
    print(f"{number3}")
elif Operatsioon == "/":
    number3 == number1 / number2
    print(f"{number3}")
else:
    print(f"{Operatsioon} Ei ole sümbol")

#11
sunni=int(input("Sünnipäev on "))
kuu=int(input("Kuu on "))
sunni2==16
kuu2==10
if sunni==sunni2 and kuu==kuu2:
    print("Täna on Juubel!")
else:
    print("Täna ei ole juubel")

#12

hinna=float(input("Hinna on "))
if hinna<10:
    uue==hinna%10
    hinna-uue
    print(f"Uue hinna on {hinna}")
elif hinna>10:
    uue2==hinna%20
    hinna-uue2
    print(f"Uue hinna on {hinna}")

#13

sugu2=input("Sugu on ").capitalize()
if sugu2=="Mees":
    aeg=float(input("Aeg on "))
    if 15<aeg<19:
        print("Jah!")
    else:
        print("Ei")
elif sugu2=="Naine":
    print("Ei")
else:
    print("?")

#14

inimesed=int(input("Inimesed on: "))
buss=int(input("Buss Inimesed on: "))
int(numbrit == 1)

while False:
    if esimesed <= buss:
        print("Buss {numbrit} on {inimesed} inimesed. See on kõik Inimesed")
    else:
        inimesed == inimesed - buss
        numbrit == numbrit + 1
        print("Buss {numbrit} on {inimesed} inimesed")
    