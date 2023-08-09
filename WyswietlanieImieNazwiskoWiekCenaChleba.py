print("Podaj swoje imię.")
imię = input()

print("Podaj swoje nazwisko.")
nazwisko = input()

wiek = int(input("Ile masz lat? "))

cena = float(input("Ile płaciłeś za chleb? "))

print()

print("Oto wprowadzone przez Ciebie dane:")
print("Imię: ", imię, ".", sep = "")
print("Nazwisko: ", nazwisko, ".", sep="")
print("Wiek:", wiek, "lata.")
print("Chleb kosztuje:", cena, "zł.")
