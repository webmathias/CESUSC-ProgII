import random
import time
import tkinter

from jogo.gato import Gato

tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=800, height=800)
canvas.pack()
gatos = [
    Gato(canvas, random.randint(0,800), random.randint(0,800)),
    Gato(canvas, random.randint(0,800), random.randint(0,800)),
    Gato(canvas, random.randint(0,800), random.randint(0,800)),
    Gato(canvas, random.randint(0,800), random.randint(0,800)),
    Gato(canvas, random.randint(0,800), random.randint(0,800)),
    Gato(canvas, random.randint(0,800), random.randint(0,800)),
    Gato(canvas, random.randint(0,800), random.randint(0,800))
]
x = 50
velocidade = 1
ultimoTempo = time.time()
while 1:
    diffTime = int((time.time() - ultimoTempo)*500)
    ultimoTempo = time.time()
    for gato in gatos:
        gato.update(canvas, diffTime)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

