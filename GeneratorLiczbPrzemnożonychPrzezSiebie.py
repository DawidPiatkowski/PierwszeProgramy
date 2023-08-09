""" Stwórz funkcję generującą w nieskończoność kolejne liczby przemnożone przez siebie tzn.:

1

4

9

16

25

36

Skorzystaj z funkcji generującej generując 20 elementów, po czym wróć od momentu skończenia i wygeneruj następnie 30 kolejnych liczb.

Zapisz wygenerowane elementy w tej samej liście.



"""

def number_multiplied_by_itself_generator():
    number = 0
    while True:
        number = number + 1
        yield number * number

generatedNumbers = []

numberGenerator = number_multiplied_by_itself_generator()

for _ in range(20):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)

"""

"""
for _ in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)    
