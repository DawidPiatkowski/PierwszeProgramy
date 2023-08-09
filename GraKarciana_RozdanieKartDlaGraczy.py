import random
 
cardList = ["9", "9", "9", "9",
"10", "10", "10", "10",
"Jack", "Jack", "Jack", "Jack",
"Queen", "Queen", "Queen", "Queen",
"King", "King", "King", "King",
"Ace", "Ace", "Ace", "Ace",
"Joker", "Joker"]
 
 
random.shuffle(cardList)
 
listaKartGracza1 = []
listaKartGracza2 = []
 
def losowanieKart(iloscKart, dlaKogo):
    for i in range(0, iloscKart):
        karta = cardList.pop()
        dlaKogo.append(karta)
 
losowanieKart(5, listaKartGracza1)
losowanieKart(5, listaKartGracza2)
 
print(listaKartGracza1)
print(listaKartGracza2)
