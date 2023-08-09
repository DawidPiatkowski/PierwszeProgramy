from random import randint
 
 
class Rocket:
    def __init__(self, name, moc):
        self.current_altitude = 0
        self.name = name
        self.moc = moc
 
    def wnoszenie(self):
        self.current_altitude += self.moc
 
 
rockets = [Rocket("Rakieta "+str(i), randint(1, 10)) for i in range(10)]
 
 
for _ in range(100):
    rockets[randint(0, 9)].wnoszenie()
 
 
for rakieta in rockets:
    print(
        rakieta.name, "o mocy", rakieta.moc,
        "znajduje się na wysokosci:", rakieta.current_altitude
        )