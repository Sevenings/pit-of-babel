import os, time, math, random
from interfaceapi import *
tela = Tela(211, 114)

circunference = Circunference(tela.getWidth()/2, tela.getHeight()/2, 20)

while True:
    tela.clear()
    tela.drawBorder()
    
    tela.drawObject(circunference)

    os.system('clear')
    print(tela.toString())
    time.sleep(0.1)
