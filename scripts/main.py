from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from hud import *
from movel import *
from menu import *
from copy import *

# Variável de controle
# Indica se o jogo está pausado ou não
playing = True

# Define as configurações da janela
janela = Window(1280, 630)
# janela = Window(1, 1) #<------ Isso aqui é só uma gambiarra minha. Liga não
janela.set_background_color((255,255,255))
janela.set_title("Paper Adventure!")
fundo = GameImage("../sprites/background.jpg")

# Define atributos da main usados nas classes
Movel.janela = Player.janela = Menu.janela = HUD.janela = janela
Player.teclado = teclado = janela.get_keyboard()
Menu.mouse = janela.get_mouse()

# Lista de armazenamento
itens = ["lapis", "borracha", "caneta", "cafe"]
plataformas = ["plataforma.jpg", "plataforma_pontilhada.png", "plataforma.jpg", "plataforma_pontilhada.png"]

# Define objetos do jogo
hud = HUD()
menu = Menu()
jogador = Player()
for i in range(4):
    plataformas[i] = Plataforma(i, i * 2)
    itens[i] = Item(itens[i], i, i * 2)
plataformas.append(Plataforma(4, 8))

# Game Loop
# Chama funções das classes para atualizar os objetos
while True:
    fundo.draw()

    # Atualiza o hud (classe HUD)
    hud.atualizar(playing)
    # Atualiza cada plataforma (classe Item)
    for plataforma in plataformas:
        plataforma.atualizar(playing)
    # Atualiza cada item (classe Item)
    for item in itens:
        item.atualizar(playing)
    # Atualiza o Stickman (classe Player)
    jogador.atualizar(plataformas, itens, playing)

    # Se pressionar ESC ou o jogo estiver pausado
    if teclado.key_pressed("ESC") or not playing:
        playing = menu.atualizar()

    janela.update()
