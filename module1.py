from math import *
from random import *


#14
size = 10
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(i * j, end=" ")
    print()








#12
algsumma = float(input("Sisestage algne summa: "))
aastad = int(input("Sisestage aastate arv: "))

intressi_määr = 5

total = algsumma
print("{:<10s}{:<12s}{:<12s}{:<12s}".format("Aasta", "Algsumma", "Intress", "Aasta lõpuks"))
for year in range(1, aastad + 1):
    interest = total * intressi_määr / 100
    total += interest
    print("{:<10d}{:<12.2f}{:<12.2f}{:<12.2f}".format(year, algsumma, interest, total))





for i in range(1, 11):
    ruut = i ** 2
    kuup = i ** 3
    print(f"{1:2} {ruut:2} {kuup:3}")




#8
paaris_arvud = 0
paaritu_arvud = 0

for arv in range(1, 101):
    if arv % 2 == 0:
        print(f"{arv} on paaris.")
        paaris_arvud += 1
    else:
        print(f"{arv} on paaritu.")
        paaritu_arvud += 1

print(f"\nPaaris arvude arv: {paaris_arvud}")
print(f"Paaritu arvude arv: {paaritu_arvud}")


#10
for arv in range(1, 101):
    if arv % 5 == 0:
        print(arv)


#7
import random

print("Loto numbrid:")
for _ in range(5):
    number = random.randint(0, 9)
    print(number, end="")




#4
print("Arvud 1-10:")
arv = 1
while arv <= 10:
    print(arv)
    arv += 1

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        tulemus = i * j
        print(f"{i} * {j} = {tulemus}")
        j += 1
    i += 1


#3

import random

kordade_arv = 10
arvude_vahemik = (1, 50)
õiged_vastused = 0

for _ in range(kordade_arv):
    arv1 = random.randint(*arvude_vahemik)
    arv2 = random.randint(*arvude_vahemik)

    vastus = int(input(f"{arv1} + {arv2} = "))

    if vastus == arv1 + arv2:
        print("Õige vastus! Hästi tehtud!")
        õiged_vastused += 1
    else:
        print(f"Vale vastus. Õige vastus on: {arv1 + arv2}")

print(f"\nTreening lõppenud! Sa said {õiged_vastused} õiget vastust {kordade_arv} küsimusest.")


#2
summa = 0
while True:
    arv = input("Sisesta arv : ") 
    if not arv:
        break
    
    summa += float(arv)

print(f"Arvude summa on: {summa}")



#1
nimi = input("Palun sisesta oma nimi: ")
kordade_arv = int(input("Sisesta, mitu korda soovid tervitatud saada: "))

for kord in range(1, kordade_arv + 1):
    print(f"Ole tervitatud, {nimi}, {kord}. korda.")


p=0
while True:
    number= int(input("Sisestage number suurem kui 10: "))
    p+=1
    if number >= 10:
        print("Õigest")
        break
    else:
        print("Arv on liiga väike",p)
print("katsed", p)
print()

n=int(input("Sisestage number n: "))
for i in range(1,11):
    print(f"{n} * {i} ={n*i}")
print()

#6
print("Kahanev kolmnurk:")
for i in range(5, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()



print("Kasvav kolmnurk:")
for i in range(1, 6):
    for j in range(i):
        print("* ", end="")
    print()



print(" 5x5 tärnid:")
for i in range(5):
    for j in range(5):
        print("* ", end="")
    print()



#5
try:
    N = int(input("Sisesta arv N: "))
    if N <= 0:
        print("Palun sisesta positiivne arv.")
    else:
        for i in range(N):
            for j in range(N):
                if i == j or i + j == N - 1:
                    print("X", end="")
                else:
                    print("O", end="")
            print()

except ValueError:
    print("Vigane sisend. Palun sisesta arv.")
except Exception as e:
    print(f"Viga: {e}")