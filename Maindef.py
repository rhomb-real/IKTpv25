import os
import glob
#1
def taisanaluus(extension: str):
    """
    Teosta täisanalüüs. Kasutaja valib laiendi. Programm käib läbi kõik failid, summeerib statistikat ja kuvab selle ekraanil.
    """
    while True:
        extension=input("Choose extension: ")
        if extension != str:
            print("Vale tüüp.")
        else:
            break
    globlist=glob.glob(f"*.{extension}")
    for i in (globlist):
        print(i.stat)

#2
def salvesta_raport_faili():
    """
    Kogu statistika kirjutatakse uude faili eespool loodud raportite kataloogi.
    """
     