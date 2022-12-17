import os, time, math
import interfaceapi as iapi

tela = iapi.Tela(211, 2*57)
pontoA = iapi.Point(tela.getWidth()/2, tela.getHeight()/2)
pontoB = iapi.Point(tela.getWidth()/2, tela.getHeight()/2)
line = iapi.Line(pontoA, pontoB)
hline = iapi.Line(iapi.Point(50, 40), iapi.Point(70, 40))

for i in range(36):
    tela.clear()
    tela.drawBorder()

    line.points[0].y -= 1
    line.points[1].y += 1

    hline.translateBy(0, 1)

    tela.drawObject(line)
    tela.drawObject(hline)

    os.system('clear')
    print(tela.toString())
    time.sleep(0.1)

time.sleep(0.5)

tela.clear()
tela.drawBorder()

i = 0
while True:
    tela.clear()
    tela.drawBorder()

    middle_point = line.middlePoint()
    line.rotateAroundPoint(middle_point, math.pi/12)

    tela.drawObject(line)

    os.system('clear')
    print(tela.toString())
    time.sleep(1/18)
    i += 1
