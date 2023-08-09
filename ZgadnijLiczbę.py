import random

def zgadnij_liczbe():
    liczba = random.randint(0, 40)
    proba = 0
    zgadniete = False
    
    print("Witaj w grze zgadnij liczbę od 0 do 40!")
    
    while not zgadniete:
        zgadnij = int(input("Podaj swoją próbę: "))
        proba += 1
        
        if zgadnij < liczba:
            print("Za mało! Spróbuj wyżej.")
        elif zgadnij > liczba:
            print("Za dużo! Spróbuj niżej.")
        else:
            zgadniete = True
            print(f"Brawo! Zgadłeś liczbę {liczba} w {proba} próbach.")

zgadnij_liczbe()
