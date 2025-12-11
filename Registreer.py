
#Registreerimine
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
        break
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
    uus_nimi=input("uus nimi: ")
    uus_parool=input("uus parool: ")
    if uus_nimi or uus_parool != type(str):
         print("Vale andmetüüp!")
    elif uus_nimi == k:
        print("Vale Nimi!")
    elif uus_parool == s:
        print("Vale parool!")
    else:
         nimi = uus_nimi
         parool = uus_parool
         break
#Paroolitaastamine
def paroolitaastamine(k: list, s: list) -> any:
    pass
parool = ""
