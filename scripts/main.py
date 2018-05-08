from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from hud import *
from item import *
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
Item.janela = Player.janela = Menu.janela = HUD.janela = janela
Player.teclado = teclado = janela.get_keyboard()
Menu.mouse = janela.get_mouse()

# Objetos base
# Vou ver se vale mais a pena copiar esses objetos ou criar objetos novos
# a cada vez que aparece um novo item / plataforma
lapis = Material("../sprites/lapis.png")
caneta = Material("../sprites/caneta.png")
borracha = Material("../sprites/borracha.png")
cafe = Material("../sprites/cafe.png")
plataforma = Item("../sprites/plataforma.jpg")
pontilhada = Item("../sprites/plataforma_pontilhada.png") # Plataforma pontilhada funciona como normal, por enquanto

# Lista de armazenamento
plataformas, itens = [], []

# Define objetos do jogo chamando com as propriedades de cada classe
hud = HUD()
menu = Menu()
jogador = Player()
itens.append(copy(lapis)) # Adiciona um lápis à lista de itens
itens.append(copy(caneta)) # Adiciona uma caneta à lista de itens
itens.append(copy(borracha)) # Adiciona uma borracha à lista de itens
itens.append(copy(cafe)) # Adiciona um cafe à lista de itens
plataformas.append(copy(plataforma)) # Adiciona uma plataforma à lista
plataformas.append(copy(pontilhada)) # Adiciona uma plataforma  pontilhada à lista
plataformas.append(copy(plataforma))
plataformas.append(copy(pontilhada))
plataformas.append(copy(plataforma))

# Configura os objetos
hud.setup()
jogador.setup()
for i in range(4): # Configura cada item
    itens[i].setup(i, i * 2)
for j in range(5): # Configura cada plataforma
    plataformas[j].setup(j, j * 2)

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

    # Se pressionar ESC
    if teclado.key_pressed("ESC"):
        playing = False
    # Se o jogo estiver pausado
    if not playing:
        # Chama o menu
        playing = Menu.atualizar()

    janela.update()
