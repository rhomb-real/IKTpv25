import glob 
import os
#1
def leia_projektifailid(extension):
    """
    Leia kõik vastava laiendiga failid.
    """
    while True:
        extension=input("File extension (.txt, .png, .py, ETC.): ")
        if extension != ".txt":
            print("Vale failitüüp!")
        else:
            break
    if extension.startswith("."):
        print("Hea.")
    else:
        extension = "."+extension
        print(extension)
    globlist=glob.glob(f"*{extension}")
    print(globlist)
#2
def analuusi_faili_sisu(File):
    """
    Loeb faili ridade kaupa.
    """
    File=input("File on: ")
    File = File+".txt"
    Count=input("Count what? ")
    normal = 0
    blank = 0
    if os.path.exists(File) == True:
        while True:
            for i in(File):
              if i.startswith("\n"):
                  blank +=1
              else:
                  normal +=1  
        File.count(Count)
        print(f"Full = {normal}, blank = {blank}, specified word = {Count}")
    else:
        print("Vale fail!")


#3
def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    """

    """
    if os.path.exists(nimi) == True:
        print("File exists")
    else:
        os.mkdir(nimi)
        print("File created")

#4
def leia_failid_algustahega(taht):
    """

    """
    while True:
     taht = input("One letter: ")
     if len(taht) > 1 or taht.isnumeric():
         print("Too many or not a letter")
     else:
         break
    four=glob.glob(taht*.*)
    print(four)
    