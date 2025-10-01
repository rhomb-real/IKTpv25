#Harjutus 1.1. Muutujad ja sisend


from traceback import print_exception


print("Tere maailm!")
nimi=input("Sisesta oma nimi: ") #sisend ja ootab enterit
print(f"Tere maailm! Tervitan sind {nimi}.")
vanus=int(input("Sisesta oma vanus: ")) #int teisendab stringi
print(f"Tere maailm! Sind {nimi}. Sa oled {vanus} aastat vana.")

#2.
#Mis tüüpi on järgnevad muutujad:
#a)vanus = 18
#b)eesnimi = "Jaak"
#c)pikkus = 16.5
#d) kas_käib_koolis = True
#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende
#Kirjuta kood tüüpide kontrollimiseks
vanus = 18
eesnimi = "Jaak"
pikkus = 1.65
kas_käib_koolis = True
print(f"vanus {vanus} on: {type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")