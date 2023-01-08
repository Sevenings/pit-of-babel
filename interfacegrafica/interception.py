from interfaceapi import *
import copy

tela = Tela()

r = Line(1, 1000, -80*1000)
s = Line(-1, -1, tela.getHeight())

p = r.interception(s)
circle = Circunference(p, 10)
tela.scene.append(circle)
tela.scene.append(Text(f'{p.x},{p.y}', Point(1, 1)))

tela.scene.append(LineSegment(r.pointOnX(0), r.pointOnY(tela.getHeight())))

i = 0
while True:
    circle.center.translateToPoint(r.pointOnX(i))
    #circle.radius = circle.center.x
    tela.update_print()
    i += 1
