k = ['Kostja', 'Nikita', 'Anja', 'Paul']
s = ['1524', 'pool', '2414', '6457']
def registreerimine(k:list, s: list) -> any:
    pass
while True:
    nimi=input("Nimi: ")
    parool=input("Parool: ")
    if nimi or parool != type(str):
        print("Vale andmetüüp!")
    elif nimi == k:
        print("Vale Nimi!")
    elif parool == s:
        print("Vale parool!")
    else:
        if parool.isdigit(any) and parool.isupper(any) and parool.islower(any):
         print("Hea!")
         break
        else: 
         print("Väle!")

#Valideerimine
def autoriseerimine(k: list, s: list) -> any:
    pass
while True:
    check_nimi=input("Nimi: ")
    check_parool=input("Parool: ")
    if check_nimi != nimi or check_parool != parool:
        print("Ei!")
    elif check_nimi or check_parool != type(str):
        print("Vale andmetüüp!")
    else:
        print("Autoriseerimine!")
        break
#Paroolivahetus
def paroolivahetus(k: list, s: list) -> any:
    pass
while True:
    chose=bool(input("0 - nimi. 1 - parool"))
    if chose != type(bool):
        print("Väle!")
    elif chose == False:
        uus_nimi=input("uus nimi: ")
        if uus_nimi != type(str):
            print("Vale andmetüüp!")
        elif uus_nimi == k:
            print("Vale Nimi!")
        else:
            nimi=uus_nimi
    else:
        uus_parool=input("uus parool: ")
        if uus_parool != type(str):
            print("Vale andmetüüp!")
        elif uus_parool == s:
            print("Vale parool!")
        else:
            parool = uus_parool
        break
#Paroolitaastamine
def paroolitaastamine(k: list, s: list) -> any:
    pass
while True:
    sure=bool(input("Are you sure? 0 - no. 1 - yes. "))
    if sure != type(bool):
       print("Väle!")
    elif sure == False:
        break
    else:
        parool = ""
        break
