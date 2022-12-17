import interfaceapi as iapi
import math, time, os

tela = iapi.Tela(211, 114)
tela.drawBorder()

xo = tela.getWidth()/2
yo = tela.getHeight()/2
radius = 25
teta_o = -math.pi/2


def flor_da_vida(dist, angle):
    tela.drawCircle("o", xo, yo, radius)
    for i in range(6):
        x = xo + (radius+dist)*math.cos(math.pi/3 * i + teta_o + angle)
        y = yo + (radius+dist)*math.sin(math.pi/3 * i + teta_o + angle)
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

