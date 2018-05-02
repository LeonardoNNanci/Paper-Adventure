from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from hud import *
from item import *
from plataforma import *
from menu import *

playing = True

janela = Window(1280, 630)
# janela = Window(1, 1)
janela.set_background_color((255,255,255))
janela.set_title("Paper Adventure!")
fundo = GameImage("../sprites/background.png")

teclado = janela.get_keyboard()

alpha = Sprite("../sprites/alpha.png")
papel = Sprite("../sprites/post-it.png")
papel.set_position((janela.width - papel.width) / 2, (janela.height - papel.height) / 2)

hud = HUD(janela)
hud.setup()

plataformas = []
for i in range(5):
    plataformas.append(Plataforma(janela))
    plataformas[i].setup(i, i * 2)

itens = []
for i in range(4):
    itens.append(Item(i, janela))
    itens[i].setup()

jogador = Player(janela)
jogador.setup()

while True:
    fundo.draw()
    hud.atualizar(playing)

    for i in range(len(plataformas)):
        plataformas[i].atualizar(playing)

    # for i in range(len(itens)):
    #     itens[i].atualizar()

    jogador.atualizar(plataformas, itens, playing)

    if teclado.key_pressed("ESC"):
        playing = False

    if not playing:
        alpha.draw()
        papel.draw()

    janela.update()
