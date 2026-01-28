from random import randint

def registreeri(k:list, s: list) -> any:
    import string
    rand=bool(input("Automaatne parool? 1-jah 0-ei: "))
    if rand == False:
       while True:
          nimi=input("Nimi: ")
          parool=input("Parool: ")
          if nimi in k:
             print("Vale Nimi!")
          elif parool in s:
             print("Vale parool!")
          else:
                 if parool.isdigit(any) and parool.isupper(any) and parool.islower(any) and parool(string.punctuation(any)):
                     print(f"Parool on {parool}")
                     k.append(nimi)
                     s.append(parool)
                     break
                 else: 
                     print("Vale parool!")
    elif rand == True:
          while True:
                 nimi=input("Nimi: ")
                 if nimi in k:
                   print("See nimi on kasutusel!")
                 else:
                  import random
                  part1 = "'~*%/()[]?#!"
                  part2 = 'qwertyuiopüõasdfghjklöäzxcvbnm'
                  part3 = '0123456789'
                  part4 = part2.upper()
                  part5 = part1 + part2 + part3 + part4
                  ls = list(part5)
                  random.shuffle(ls)
                  parool = "".join(ls)
                  print(f"Parool on {parool}")
                  k.append(nimi)
                  s.append(parool)
                  break
    else:
     print("Vale andmetüüp!")

#Valideerimine
def autoriseerimine(k: list, s: list) -> any:
    while True:
         check_nimi=input("Nimi: ")
         check_parool=input("Parool: ")
         if check_nimi not in k or check_parool not in s:
            print("Vale info!")
         else:
            if check_parool == s[k.index(check_nimi)]:
               print("Autoriseerimine!")
               break
            else:
               print("Nimi ja parool ei sobi kokku!")
#Paroolivahetus
def paroolivahetus(k: list, s: list) -> any:
    import string
    kontroll = ("Sisesta konto nimi")
    if kontroll not in k:
        print("Ei ole konto!")
    else:
        while True:
         valik=bool(input("(0 - nimi. 1 - parool) valik: "))
         if valik == False:
                uus_nimi=input("uus nimi: ")
                if uus_nimi in k:
                    print("Vale Nimi!")
                else:
                  k[k.index(kontroll)] = uus_nimi
                  print(k)
         else:
               uus_parool=input("uus parool: ")
               if uus_parool in s:
                 print("Parool kasutusel!")
               else:
                 if uus_parool.isdigit(any) and uus_parool.isupper(any) and uus_parool.islower(any) and uus_parool(string.punctuation(any)):
                   s[k.index(kontroll)] = uus_parool
                   print(s)
                 else:
                    print("Vale!")
                    break
#Paroolitaastamine
def paroolitaastamine(k: list, s:list) -> any:
    while True:
        akkaunt = input("Akkaunt nimi: ")
        kindel=bool(input("Oled sa kindel? 0 - no. 1 - yes. "))
        if kindel == False:
            print("Toimingu tühistamine. . .")
            break
        else:
            s[k.index(akkaunt)] = ""
            print("Parool taastamine.")
            break


