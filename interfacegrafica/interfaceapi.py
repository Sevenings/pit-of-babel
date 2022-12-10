import os
import time
import math

class Tela:
    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.surface = []
        for i in range(y):
            self.surface.append([])
            for j in range(x):
                self.surface[i].append(" ")
        self.surface_save = self.surface.copy()
    
    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                self.surface[i][j] = ' '

    def toString(self):
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                output += self.surface[i][j]
            output += "\n"
        return output

    def drawPoint(self, character, x, y):
        if x >= self.width or x < 0:
            return False
        if y >= self.height or y < 0:
            return False
        self.surface[y][x] = character
        return True

    def drawLine(self, character, xo, yo, length):
        for i in range(length):
            self.drawPoint(character, xo + i, yo)

    def drawCollumn(self, character, xo, yo, height):
        for j in range(height):
            self.drawPoint(character, xo, yo + j)

    def drawDivisionLine(self, character, yo):
        self.drawLine(character, 0, yo, self.width)

    def drawDivisionCollumn(self, character, xo):
        self.drawCollumn(character, xo, 0, self.height)

    def drawBorder(self, cornerChar='@', horizontalChar='-', verticalChar='|'):
        self.drawDivisionLine(horizontalChar, 0)
        self.drawDivisionLine(horizontalChar, self.height-1)
        self.drawDivisionCollumn(verticalChar, 0)
        self.drawDivisionCollumn(verticalChar, self.width-1)
        self.drawPoint(cornerChar, 0, 0)
        self.drawPoint(cornerChar, 0, self.height-1)
        self.drawPoint(cornerChar, self.width-1, 0)
        self.drawPoint(cornerChar, self.width-1, self.height-1)

    def write(self, text, xo, yo):
        for i in range(len(text)):
            self.drawPoint(text[i], xo+i, yo)

    def drawCircle(self, char, xo, yo, radius):
        for i in range(360):
            x = int(xo + radius*math.cos(math.pi/180 * i))
            y = int(yo + radius/2*math.sin(math.pi/180 * i))
            self.drawPoint(char, x, y)


tela = Tela(211, 57)
tela.drawBorder()

xo = tela.width/2
yo = tela.height/2
radius = 25
teta_o = -math.pi/2


def flor_da_vida(dist, angle):
    tela.drawCircle("o", xo, yo, radius)
    for i in range(6):
        x = xo + (radius+dist)*math.cos(math.pi/3 * i + teta_o + angle)
        y = yo + (radius+dist)/2*math.sin(math.pi/3 * i + teta_o + angle)
        tela.drawCircle("o", x, y, radius)

for i in range(120):
    tela.clear()
    tela.drawBorder()
    os.system('clear')

    flor_da_vida(120-i, 0)

    print(tela.toString())
    time.sleep(0.1)

i = 0
while True:
    tela.clear()
    tela.drawBorder()
    os.system('clear')

    flor_da_vida(0, i*math.pi/180)

    print(tela.toString())
    time.sleep(0.1)
    i += 1
