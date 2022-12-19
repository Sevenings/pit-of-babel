from interfaceapi import *
import copy

tela = Tela()

triangle = Polygon(Point(30, 80), Point(120, 80), Point(90, 28))
triangle.translateToPoint(tela.center() + Point(0, 10))
bis_point = copy.copy(triangle.points[0])
bissetrix = LineSegment(triangle.points[0], bis_point)
circunference = Circunference(bis_point, )


tela.addObject(Text("Incenter", tela.center() + Point(-10, 35)))
tela.addObject(triangle)
tela.addObject(bissetrix)

while True:
    bis_point.translateBy(1.5, -0.3)
    tela.update_print()
