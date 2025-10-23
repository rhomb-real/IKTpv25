from traceback import _ExceptionPrintContext


print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Mis sinu nimi on? ").capitalize()
print(f"{nimi}, oi kui ilus nimi!")
try:
    kusimus=bool(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if kusimus == 1:
        print("Indeksi leidmine")
        while true:
            try:
                 pikkus=float(input("Sinu pikkus on: "))
                 if 0 < pikkus <= 250:
                     break
                 else:
                     print("Pikkus peabolema vahemikus 0 kuni 250 cm!")
            except:
                 print("Vale pikkuse formaat! Palun sisesta täisarv")
        while true:
            try:
                mass = float(input("Mis on sinu kaal? "))
                if 0 < mass <= 200:
                    break
                else:
                    print("Kaal peab olema vahemikus 0 kuni 200 kg!")
            except:
                print("Vale kaalu formaat! Palun sisesta arv.")
        calc = round(mass / (0.01 * pikkus) ** 2, 2)
        print(f"{nimi}! Sinu keha indeks on: {index}")
    elif kusimius == 0:
        print("Kahju! See on väga kasulik info!")
        print("")
    else:
        print("See pole kehtiv vastus! Palun, vastake jah-vastuse korral 1 ja ei-vastuse korral 0.")
        print("")
except:
    print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")