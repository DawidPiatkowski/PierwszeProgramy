print("Obliczanie pola i obwodu koła")


r = float(input("Podaj promień r: "))
a = float(input("Podaj bok a: "))

Pi = 3.1415

Obwod = 2 * Pi * r
Pole = Pi * r**2
PoleKwadrat = a**2
ObwodKwadratu = 4 * a
          
print()

          
print("Dla r: ", r, "pole i obwód koła wynosi:", Pole, "i", Obwod)
print("Pole i obwód wynoszą odpowiednio dla a=", a, "-", PoleKwadrat, "i", ObwodKwadratu) 
