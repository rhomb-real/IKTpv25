
paev = input("Sisesta p�eva nimetus (n�iteks esmasp�ev): ")
#1 Kui on neljap�ev, siis "Huraa, programmeerimine!"
if paev.lower()=="neljap�ev":
    pring("Huraaa, Programmeerimine!")

#2. Kui on neljap�ev, siis "Huraa, programmeerimine!", siis "Igatsen, programmeerimine tahaks!"

if paev.lower() =="neljap�ev":
    pring("Huraaa, Programmeerimine!")
else:
    print("Igatsen, programmeerida tahaks!")

#3. t��paevad ja n�dalavahetus
if paev.lower()=="laup�ev" or paev.lower()=="p�hap�ev":
    print("L�puks ometi n�dalavahetus")
else:
    pring("T��p�ev, pean t��l k�ima!")