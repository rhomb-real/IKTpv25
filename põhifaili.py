from Registreer import *
k = ['Kostja', 'Nikita', 'Anja', 'Paul']
s = ['1524', 'pool', '2414', '6457']

while True:
    print("Vali tegevus:")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Paroolihavetus")
    print("4 - Paroolitaastamine")
    print("5 - Välju")
    valik = input("Sisesta valik (1-5): ")
    if valik == '1':
        registreerimine(k, s)
    elif valik == '2':
        autoriseerimine(k, s)
    elif valik == '3':
        paroolivahetus (k, s)
    elif valik == '4':
        paroolitaastamine (k, s)
    elif valik == '5':
        print ("Väljun programmist")
    else:
        print ("Vale number!")