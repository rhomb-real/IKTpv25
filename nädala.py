
paev = input("Sisesta päeva nimetus (näiteks esmaspäev): ")
#1 Kui on neljapäev, siis "Huraa, programmeerimine!"
if paev.lower()=="neljapäev":
    print("Huraaa, Programmeerimine!")

#2. Kui on neljapäev, siis "Huraa, programmeerimine!", siis "Igatsen, programmeerimine tahaks!"

if paev.lower() =="neljapäev":
    print("Huraaa, Programmeerimine!")
else:
    print("Igatsen, programmeerida tahaks!")

#3. tööpaevad ja nädalavahetus
if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus")
else:
    print("Tööpäev, pean tööl käima!")