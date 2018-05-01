from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from hud import *
from item import *
from plataforma import *

janela = Window(1280, 630)
# janela = Window(1, 1)
janela.set_background_color((255,255,255))
janela.set_title("Paper Adventure!")
fundo = GameImage("../sprites/background.png")
hud = HUD(janela)
hud.setup()

plataforma1 = Plataforma(janela, 0)
plataforma1.setup(0, 13)

plataforma2 = Plataforma(janela, 1)
plataforma2.setup(15, 10)

itens = []
for i in range(4):
    itens.append(Item(i, janela))
    itens[i].setup()
    
jogador = Player(janela)
jogador.setup()

while True:
    fundo.draw()
    hud.atualizar()
    plataforma1.atualizar()
    plataforma2.atualizar()
    for i in range(4):
        itens[i].atualizar()
    jogador.atualizar()
    janela.update()
