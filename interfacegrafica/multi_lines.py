import os, time, math, random
from interfaceapi import *
tela = Tela(211, 114)

class MovableTriangle(Triangle):
    def __init__(self, A: Point, B: Point, C: Point):
        super().__init__(A, B, C)
        self.angle_speed = math.pi/12*(random.random()*2 - 1)
        self.speed = [3*(random.random()*2 - 1), 3*(random.random()*2 - 1)]
        
    def setSpeed(self, speed):
        self.speed = speed

A = Point(40, 40)
B = Point(50, 15)
C = Point(30, 27)

triangle = MovableTriangle(A, B, C)

triple_angle = MovableTriangle(Point(20, 43), Point(47, 24), Point(25, 65))
tres_angulos = MovableTriangle(Point(200, 90), Point(180, 90), Point(190, 75))

shapes = [triangle, triple_angle, tres_angulos]

while True:
    tela.clear()
    tela.drawBorder()

    #A.rotateAroundPoint(B, math.pi/20)
    for trilateral in shapes:
        for corner in trilateral.points:
            if corner.x > tela.getWidth():
                trilateral.speed[0] = -1*abs(trilateral.speed[0])
                trilateral.angle_speed *= -1
            elif corner.x < 0:
                trilateral.speed[0] = abs(trilateral.speed[0])
                trilateral.angle_speed *= -1
            if corner.y > tela.getHeight():
                trilateral.speed[1] = -1*abs(trilateral.speed[1])
                trilateral.angle_speed *= -1
            elif corner.y < 0:
                trilateral.speed[1] = abs(trilateral.speed[1])
                trilateral.angle_speed *= -1

        trilateral.rotateAroundPoint(trilateral.baricenter(), trilateral.angle_speed)
        trilateral.translateBy(trilateral.speed[0], trilateral.speed[1])

        tela.drawObject(trilateral)

    os.system('clear')
    print(tela.toString())
    time.sleep(0.1)
