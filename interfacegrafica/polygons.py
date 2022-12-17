import os, time, math, random
from interfaceapi import *
tela = Tela(211, 114)



star = Star(tela.center(), 25)
star = RegularPolygon(tela.center(), 5, 25, -math.pi/10, 2)
circle = Circunference(tela.center().x, tela.center().y, 26)
pentagon = RegularPolygon(tela.center(), 5, 35)
hexagon = RegularPolygon(tela.center(), 6, 50, math.pi)
u_pentagon = RegularPolygon(tela.center(), 5, 43, 1*math.pi/5)

scene = [
        RegularPolygon(tela.center(), 3, 100),
        RegularPolygon(tela.center(), 3, 100, math.pi),
        star, 
        circle, 
        hexagon, 
        pentagon, 
        u_pentagon,
        Circunference(tela.center().x, tela.center().y, 50),
        Circunference(tela.center().x, tela.center().y, 43)
        ]


while True:
    tela.clear()
    tela.drawBorder()
  
    scene[0].rotate(-math.pi/320)
    scene[1].rotate(-math.pi/320)
    star.rotate(-math.pi/80)
    pentagon.rotate(math.pi/80)
    u_pentagon.rotate(math.pi/80)


    for object in scene:
        tela.drawObject(object)

    os.system('clear')
    print(tela.toString())
    time.sleep(0.1)
