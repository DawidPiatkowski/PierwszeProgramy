from tkinter import *

t = Tk()
t.title("Wybierz przycisk")
t.geometry("400x650")

import random

def wstawPrzyciski():
    ilePrzyciskow = 8
    global przyciski
    przyciski = []
    dobry = random.randint(0, ilePrzyciskow - 1)
    for i in range (ilePrzyciskow):
        if i == dobry:
            przyciski.append(Button(t, text = "kliknij mnie", command = trafiony))
        else:
            przyciski.append(Button(t, text = "kliknij mnie", command = pudło))
        for i in przyciski:
            i.pack(fill = BOTH, expand = YES)


def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Trafiłeś dobry przycisk")
    etykieta.pack(fill = BOTH, expand = YES)

def restart():
    etykieta.destroy()
    wstawPrzyciski()

def pudło():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Trafiłeś zły przycisk")
    etykieta.pack(fill = BOTH, expand = YES)
    t.after(5000, restart)
