
#1
print("Tere maailm!")
nimi=input("Sisesta oma nimi: ") #sisend ja ootab enterit
print(f"Tere maailm! Tervitan sind {nimi}.")
vanus=int(input("Sisesta oma vanus: ")) #int teisendab stringi
print(f"Tere maailm! Sind {nimi}. Sa oled {vanus} aastat vana.")

#2
vanus = 18 #int
eesnimi = "Jaak" #string
pikkus = 1.65 #float
kas_käib_koolis = True #bool
print(f"vanus {vanus} on: {type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")

#3
import math
import random


kommid = random.randint(0, 10)
print(f"Kommid on {kommid}.")
sub=int(input("Mitu kommi võta? "))
kommid = kommid - sub
print(f"Kommid on {kommid}.")

#4
circle = int(input("kui pikk on ringjoon?  "))
diam = circle / 3.15
print(f"Ring diameter on {diam}")

#5
N=int(input("mis on N? "))
m=int(input("Mis on m? "))
diag = (m * N) ** 2 + (m * m) ** 2 
print(f"diag = {math.sqrt(diag)}")


#6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print(f"Sinu kiirus oli {kiirus} km/h") #str(kiirus)

#7

import statistics
from statistics import mean

d = [5, 10, 15, 20, 25]
x = mean(d)
sum = sum(d)
div=int(input("div on? "))
res = sum / div
print(f"result on {res}, mean on {x}")

#8

print("""\         @..@
         (----)
        ( \__/ )
        ^^ "" ^^  
                 """)

#9

a=int(input("mis a on? "))
b=int(input("mis b on? "))
c=int(input("mis c on? "))
P = a + b + c
print(f"P on {P}")

#10

I=int(input("Mitu on inimest? "))
Cash = (0.1 * 12.90) / I
print(f"Raha on {Cash}")
