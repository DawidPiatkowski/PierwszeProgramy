import pygame
import os
import random
import math

pygame.init()

widt = 1400
hight = 800
screen = pygame.display.set_mode((widt, hight))

def write(text, x, y, size):
    cz = pygame.font.SysFont("Arial", size)
    rend = cz.render(text, 1, (255, 100, 100))
    x = (widt - rend.get_rect().width)/2
    y = (hight - rend.get_rect().height)/1.1
    screen.blit(rend, (x, y))
    
whatShow = "menu"


class Obstacle():
    def __init__(self, x, szerokosc):
        self.x = x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.hight_gora = random.randint(50, 300)
        self.odstep = 400
        self.y_dol = self.hight_gora + self.odstep
        self.hight_dol = hight - self.y_dol        
        self.kolor = (160, 140, 190)
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.hight_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.hight_dol)
    def draw(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt_gora, 0)
        pygame.draw.rect(screen, self.kolor, self.ksztalt_dol, 0)
    def movement (self, v):
        self.x = self.x - v
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.hight_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.hight_dol)
    def collision(self, player):
        if self.ksztalt_gora.colliderect(player) or self.ksztalt_dol.colliderect(player):
            return True
        else:
            return False
        
class Helicopter():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wysokosc = 20
        self.szerokosc = 40
        self.ksztalt = pygame.Rect(self.x, self.y, self.szerokosc, self.wysokosc)
        self.graphics = pygame.image.load(os.path.join("helicopter.png"))
    def draw(self):
            screen.blit(self.graphics, (self.x, self.y))
    def movement(self, v):
            self.y = self.y + v
        
obstacles = []
for i in range(21):
    obstacles.append(Obstacle(i * widt / 20, widt / 20))

player = Helicopter(250, 275)
dy = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
            if event.key == pygame.K_SPACE:
                if whatShow != "rozgrywka":
                    player = Helicopter(250, 275)
                    dy = 0
                    whatShow = "rozgrywka"
                    points = 0
    if whatShow == "menu":
        write("Naciśnij spację, aby zacząć", 80, 150, 40)
        graphics = pygame.image.load(os.path.join("obraz.png"))
        screen.blit(graphics, (100, 100))
    elif whatShow == "rozgrywka":
        for p in obstacles:
            p.movement(1)
            p.draw()
            if p.collision(player.ksztalt):
                whatShow = "koniec"
        for p in obstacles:
            if p.x <= -p.szerokosc:
                obstacles.remove(p)
                obstacles.append((Obstacle(widt, widt / 40)))
                points = points + math.fabs(dy)
        player.draw()
        player.movement(dy)
        write(str(points), 50, 50, 20)

    elif whatShow == "koniec":
        graphics = pygame.image.load(os.path.join("obraz.png"))
        screen.blit(graphics, (50, 50))
        write("Niestety przegrywasz z kretesem", 50, 290, 40)
        write("Naciśnij spację aby zagrać jeszcze raz", 100, 100, 40)
        write("Twój wynik to: " + str(points), 50, 320, 20)
    pygame.display.update()
