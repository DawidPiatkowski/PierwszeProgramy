"""
Napisz program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
"""
definicje = {}

def dodaj_definicje():
    slowo = input("Podaj słowo, dla którego chcesz dodać definicję: ")
    definicja = input(f"Podaj definicję dla słowa '{slowo}': ")
    definicje[slowo] = definicja
    print(f"Definicja dla słowa '{slowo}' została dodana.")

def szukaj_definicji():
    slowo = input("Podaj słowo, dla którego chcesz znaleźć definicję: ")
    if slowo in definicje:
        print(f"Definicja dla słowa '{slowo}': {definicje[slowo]}")
    else:
        print(f"Brak definicji dla słowa '{slowo}'.")

def usun_definicje():
    slowo = input("Podaj słowo, dla którego chcesz usunąć definicję: ")
    if slowo in definicje:
        del definicje[slowo]
        print(f"Definicja dla słowa '{slowo}' została usunięta.")
    else:
        print(f"Brak definicji do usunięcia dla słowa '{slowo}'.")

def menu():
    print("Witaj w programie zarządzania definicjami słów!")
    while True:
        print("\nMenu:")
        print("1. Dodaj nową definicję")
        print("2. Szukaj istniejącej definicji")
        print("3. Usuń wybraną definicję")
        print("4. Zakończ program")
        wybor = input("Wybierz opcję (1/2/3/4): ")
        
        if wybor == '1':
            dodaj_definicje()
        elif wybor == '2':
            szukaj_definicji()
        elif wybor == '3':
            usun_definicje()
        elif wybor == '4':
            print("Dziękujemy za korzystanie z programu!")
            break
        else:
            print("Niepoprawny wybór. Wybierz opcję 1, 2, 3 lub 4.")

if __name__ == "__main__":
    menu()
