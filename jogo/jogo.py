import random
import time
import tkinter

from gato import Gato
from ponto import Ponto
tk = tkinter.Tk()
canvas = tkinter.Canvas(tk, width=800, height=800)
canvas.pack()
gatos = [
    Gato(canvas, random.randint(0,800), random.randint(0,800))
]
ultimoClick = Ponto(0,0)
#Função de callback para quando clicar com o Mouse
def callback(event):
    ultimoClick.x = event.x
    ultimoClick.y = event.y

canvas.bind("<Button-1>", callback)
ultimoTempo = time.time()
while 1:
    diffTime = int((time.time() - ultimoTempo)*500)
    ultimoTempo = time.time()
    for gato in gatos:
        gato.update(canvas, diffTime/1000,ultimoClick)
    tk.update()
    time.sleep(0.03)

