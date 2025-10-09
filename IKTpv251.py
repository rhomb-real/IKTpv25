import math
from math import * #import oli valesti tehtud
print("Ruudu karakteristikud")
a=int(input("Sisesta ruudu külje pikkus => ")) #int
S=a**2
print(f"Ruudu pindala {S}")
P=4*a
print(f"Ruudu ümbermõõt {P}")
di=a*math.sqrt(2) #sqrT, ei sqr, import sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=int(input("Sisesta ristküliku 1. külje pikkus => ")) #int
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #float
Ss=b*c #nimi
print(f"Ristküliku pindala {Ss}")
Ps=2*(b+c) #nimi
print(f"Ristküliku ümbermõõt {Ps}")
di=math.sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di, 2)) #numbrit
print()
print("Ringi karakteristikud")
r=int(input("Sisesta ringi raadiusi pikkus => ")) #int
d=2*r
print(f"Ringi läbimõõt {d}")
Sr=pi*r*2 #import pi, nimi
print("Ringi pindala", round(Sr, 2)) #numbrit
C=2*pi*r
print("Ringjoone pikkus", round(C, 2)) #numbrit