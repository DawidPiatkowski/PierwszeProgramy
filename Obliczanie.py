#obliczanie sumy, różnicy, ilorazu i iloczynu a i b.Obliczanie reszty z dzielenia a modulo b i pierwiastek z a+b.

import math

a = 100
b = 50

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("pierwiastek z a + b = ", math.sqrt(a + b))

print()
print()
print()

import math

a = int(input("Podaj a = "))
b = int(input("Podaj b = "))

#Podawanie wartośco a i b (liczby calkowite)
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("pierwiastek z a + b = ", math.sqrt(a + b))

print()
print()
print()

#Obliczanie obwod i pole prostokata
a = int(input("Podaj a = "))
b = int(input("Podaj b = "))
print("Pole = ", a*b)
print("Obwód = ", 2 * a + 2 * b)
