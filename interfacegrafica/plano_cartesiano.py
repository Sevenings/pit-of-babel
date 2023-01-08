from interfaceapi import *

tela = Tela()

tela.drawDivisionLine('-', tela.center().y)
tela.drawDivisionCollumn("|", tela.center().x)

print(tela.toString())
