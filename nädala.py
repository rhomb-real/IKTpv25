
paev = input("Sisesta päeva nimetus (näiteks esmaspäev): ")
#1 Kui on neljapäev, siis "Huraa, programmeerimine!"
if paev.lower()=="neljapäev":
    pring("Huraaa, Programmeerimine!")

#2. Kui on neljapäev, siis "Huraa, programmeerimine!", siis "Igatsen, programmeerimine tahaks!"

if paev.lower() =="neljapäev":
    pring("Huraaa, Programmeerimine!")
else:
    print("Igatsen, programmeerida tahaks!")

#3. tööpaevad ja nädalavahetus
if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus")
else:
    pring("Tööpäev, pean tööl käima!")