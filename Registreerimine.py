from random import randint

k =  []
s =  []
def registreeri(k:list, s: list) -> any:
    import string
    parool = ""
    rand=bool(input("Automaatne parool? 1-jah 0-ei: "))
    if rand == False:
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
                 if parool.isdigit(any) and parool.isupper(any) and parool.islower(any) and parool(string.punctuation(any)):
                     print(f"Parool on {parool}")
                     regi = 1
                     break
                 else: 
                     print("Vale parool!")
    elif rand == True:
          while True:
                 nimi=input("Nimi: ")
                 if nimi != type(str):
                    print("Vale andmetüüp!")
                 elif nimi == k:
                   print("Vale nimi!")
                 else:
                  import random
                  part1 = "'~*%/()[]?#!"
                  part2 = 'qwertyuiopüõasdfghjklöäzxcvbnm'
                  part3 = '0123456789'
                  part4 = part2.upper()
                  part5 = part1 + part2 + part3 + part4
                  ls = list(part5)
                  random.shuffle(ls)
                  parool == ls
                  print(f"Parool on {parool}")
                  regi =1
                  break
    else:
     print("Vale andmetüüp!")

#Valideerimine
def autoriseerimine(k: list, s: list) -> any:
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
    import string
    if regi == 1:
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
                if uus_parool.isdigit(any) and uus_parool.isupper(any) and uus_parool.islower(any) and uus_parool(string.punctuation(any)):
                    parool = uus_parool
                else:
                    print("Väle")
                    break
    else:
        print("Ei ole akkaunt!")
#Paroolitaastamine
def paroolitaastamine(k: list, s: list) -> any:
    while True:
        sure=bool(input("Are you sure? 0 - no. 1 - yes. "))
        if sure != type(bool):
           print("Väle!")
        elif sure == False:
            break
        else:
            parool = ""
            break


