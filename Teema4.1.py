t=['a', 'e', 'i', 'o', 'u', 'ü', 'ä', 'ö', 'õ']
k=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
m=string.punctuation + string.whitespace
laus = input("Sinu laus on: ").lower()
täishäälkus=0
kaashäälkud=0
märgid=000

for täht in laus:
    if täht in t:
        täishäälkud+=1
    elif täht in k:
        kaashäälkud+=1
    elif täht in m:
        märgid+=1
print(f"{täishäälkud}, {kaashäälkud}, ja {märgid}")

#2
names = []

for i in range(5):
    ask = input("Sisesta palun 5 nime: ").split()
    names.append(ask)

print(names)
vimane_nimi = names[-1]
names.sort()
print(f"the names are: {names}")
print(vimane_nimi)

replace = input("Kas sa tahad muuta nimi? ")
if replace == "Jah":
    vana_nimi = input ("Mis nimi muutane?")
    uus_nimi = input ("Mis uus nimi?")
    find = names.index(vana_nimi)
    names[find] = uus_nimi
    print(names)
else:
    print(names)

vanused = [25, 30, 22, 28, 35, 30, 22]
suurem = max(vanused)
väiksem = min(vanused)
sum = sum(vanused)
#keskel = 
print(f"suurem on {suurem}, väiksem on {väiksem}, sum on {sum}, keskel on {keskel}")

#3
num = []
star = "*"
for i in range(6):
    mult = int(input("Multipliers: "))
    num.append(mult)
for i in range (6):
    starmult = star * min(num)
    num.remove(min(num))
    num.append(starmult)
print(f"{num}")
 
#4
indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa,Lääne-Virumaa,Jõgeva"]
while True:
    try:
        index=int(input("Sisesta oma postiindeks: "))
        if 10000<=index<=99999:
            break
        else:
            print("Postiindeks peab olema 5-kohaline arv")
    except:
        print("Vigane andmetüüp.")
index_list=list(index)
n1=int(index_list[0])
print(f"Sinu postiindeksiga {index} kuulud piirkonda: {indexid[n1-1]}")
if n1 in [0,1,2,7]:
    print("Mine merre!")
else:
    print("Mine metsa!")

#5
import random
loend_arvud=[]
loend_tähed=[]
mitu=random.randint(2,20)
for i in range(mitu):
    elem=random.randint(1,100)
    loend_arvud.append(elem)
    elem=chr(randint(65,90))
print(f"Kokku on {mitu} elemente loendis")
while True:
    try:
        paaride_arv=int(input(f"Sisesta mitu paari soovid vahetada: "))
        if 1<=paaride_arv<=mitu//2:
            break
        else:
            print(f"Arv peab olema vahemikus 1 kuni {mitu//2}")
    except:
        print("Vigane andmetüüp, proovi uuesti")

#cycle = int(input("Count: "))
#rer = []
#for i in range(cycle):
 #   rev = int(input("Numbers: "))
  #  rer.append(rev)
#rer.reverse
#print(rer)

#6
suurim = max(loend_arvud)
kus_asub=loend_arvud.index(suurim)
suurim_muudatud = suurim/mitu
loend_arvud[kus_asub] = round(suurim_muudatud,2)
print(f"Muutmise järel: {loend_arvud}")
