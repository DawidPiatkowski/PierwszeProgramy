from tkinter import *
import random

t = Tk()
t.title("Wybierz przycisk")

t.geometry("400x650")


def wstawPrzyciski():
    ilePrzyciskow = 4
    global przyciski
    przyciski = []
    dobry = random.randint(0, ilePrzyciskow - 1)
    for i in range (ilePrzyciskow):
        if i == dobry:
            przyciski.append(Button(t, text = "kliknij mnie", command = trafiony))
        else:
            przyciski.append(Button(t, text = "kliknij mnie", command = pudlo))
        for i in przyciski:
            i.pack(fill = BOTH, expand = YES)

def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Trafiłeś dobry przycisk")
    #wygrana()
    etykieta.pack(fill = BOTH, expand = YES)
    
"""
def wygrana():
    ilePrzyciskow = 2
    global przyciski
    przyciski = []
    dobry = random.randint(0, ilePrzyciskow - 1)
    for i in range (ilePrzyciskow):
        if i == dobry:
            return wstawPrzyciski()
        else:
            przyciski.append(Button(t, text = "NIE", command = koniec))
        for i in przyciski:
            i.pack(fill = BOTH, expand = YES)
    
def koniec():
    pass

    """

def restart():
    etykieta.destroy()
    wstawPrzyciski()

def pudlo():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Trafiłeś zły przycisk")
    etykieta.pack(fill = BOTH, expand = YES)
    t.after(500, restart)
    
wstawPrzyciski()
