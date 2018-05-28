from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from hud import *
from menu import *
from itens import *
from random import randint

########### Funções Auxiliares ##############################################
def criar_objs(plataformas, itens, timer):

    # Testa o intervalo entre a criação dos objetos
    if janela.time_elapsed() - timer >= 1500:
        # Cria uma plataforma nova
        plataformas.append(Plataforma(randint(0, 4), width = randint(janela.width / 5, janela.width / 2)))
        # Calcula a quantidade de itens na plataforma
        qtd_itens = int(plataformas[-1].width / 88)
        plt = plataformas[-1]

        # Cria os itens em cima da plataforma
        for i in range(qtd_itens):
            aux = randint(0, 100)
            if aux < 1: # 1% de chance de aparecer um café
                itens.append(Cafe(plt.x + 88 * i, plt.y))
            elif aux < 2: # 1% de chance de aparecer uma caneta
                itens.append(Caneta(plt.x + 88 * i, plt.y))
            if aux < 30 and i == 0: # 28% de chance de aparecer uma borracha (se for borracha, vai ser o único item na plataforma)
                itens.append(Borracha(plt.x + 88 * i, plt.y, plt))
                break
            elif aux < 75: # 45% de chance de aparecer um lápis
                itens.append(Lapis(plt.x + 88 * i, plt.y))
            # 25% de chance de não ter item nenhum

            timer = janela.time_elapsed()

    return timer # Passa o tempo atual para o controle de criação

# Atualiza cada plataforma
def atualizar_plataformas(lista):
    jogador.colisao = False
    for i in range(len(lista) - 1, -1, -1):
        lista[i].atualizar(jogador, playing)
        # Se estiver fora da tela, deixa de existir
        if lista[i].x < -lista[i].width:
            lista.pop(i)

# Atualiza cada item
def atualizar_itens(lista):
    for j in range(len(lista) -1, -1, -1):
        # Atualiza e checa se teve colisão com o jogador
        if lista[j].atualizar(jogador, playing):
            # Ativa o efeito do item
            lista[j].efeito(jogador)
            # Se for borracha, não some
            if lista[j].__class__.__name__ != "Borracha":
                lista.pop(j)
        elif lista[j].x < -lista[j].width:
            lista.pop(j)

##############################################################################

########### Função Principal #################################################
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
Movel.x_vel = Borracha.x_vel = janela.width / 7

itens, plataformas = [], []

# Define objetos do jogo
hud = HUD()
menu = Menu()
jogador = Player()
plataformas.append(Plataforma(0, 0))
itens.append(Borracha(0, 0, plataformas[0]))
itens.append(Cafe(1, 2))
itens.append(Caneta(2, 4))
itens.append(Lapis(3, 6))
timer = 0

# Game Loop
# Chama funções das classes para atualizar os objetos
while True:
    fundo.draw()

    # Atualiza o hud (classe HUD)
    hud.atualizar(playing)

    # Atualiza o Stickman (classe Player)
    jogador.atualizar(plataformas, itens, playing)

    # Atualiza cada plataforma (classe Item)
    atualizar_plataformas(plataformas)

    # Atualiza cada item (classe Item)
    atualizar_itens(itens)

    # Se pressionar ESC ou o jogo estiver pausado
    if teclado.key_pressed("ESC") or not playing:
        playing = menu.atualizar()

    janela.update()

    # Controle de criação de novos objetos
    timer = criar_objs(plataformas, itens, timer)
