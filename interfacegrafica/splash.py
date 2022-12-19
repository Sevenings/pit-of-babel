from interfaceapi import *
from random import randint

class Splash:
    def __init__(self, origin, life, speed, generation):
        self.origin = origin
        self.life = life
        self.speed = speed
        self.age = 0
        self.generation = generation
    
    def draw(self, tela):
        tela.drawCircle('~', self.origin.x, self.origin.y, self.age*self.speed)
        if self.generation < 3 and self.age > self.life*0.25:
            tela.scene.append(Splash(self.origin, self.life, self.speed, self.generation + 1))
            self.generation = 3
        if self.age < self.life:
            self.age += 1
        else: 
            tela.scene.remove(self)


tela = Tela()

i = 0
while True:
    if randint(1, 10) == 1:
        origin = Point(randint(0, tela.getWidth()), randint(0, tela.getHeight()))
        life = randint(10, 35)
        speed = 0.8
        tela.scene.append(Splash(origin, life, speed, 1))
    tela.update_print()
    i += 1
