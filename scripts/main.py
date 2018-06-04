from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from player import *
from hud import *
from menu import *
from itens import *
from random import randint

########### Funções Auxiliares ##############################################
def mover_objs(jogador, plataformas, itens):
    for plataforma in plataformas:
        plataforma.mover()
    for item in itens:
        item.mover()
    jogador.mover()

def colisoes_objs(jogador, plataformas, itens):
    jogador.colisao = False
    for plataforma in plataformas:
        if plataforma.colisao(jogador.controler) and jogador.y_vel >= 0 and jogador.colisao == False:
            if plataforma.y_vel != 0:
                jogador.y_vel = plataforma.y_vel + (Pontilhada.gravidade * janela.delta_time())
            else:
                jogador.y_vel = 0
            jogador.colisao = True

    for i in range(len(itens) - 1, -1, -1):
        if itens[i].colisao(jogador.cur_sprt):
            itens[i].efeito(jogador)
            if itens[i].__class__.__name__ != "Borracha":
                itens.pop(i)


def atualizar_objs(player, plataformas, itens):
    for i in range(len(plataformas) - 1, -1, -1):
        if plataformas[i].x < -plataformas[i].width or plataformas[i].y > janela.height + plataformas[i].height + jogador.cur_sprt.height:
            plataformas.pop(i)

    for j in range(len(itens) - 1, -1, -1):
        if itens[j].x < -itens[j].width or itens[j].y > janela.height + itens[j].height:
            itens.pop(j)

    # Controle do tempo de duração do efeito da Caneta
    # Se passar o tempo
    if janela.time_elapsed() - Caneta.timer >= Caneta.t_efeito and Caneta.ativo:
        jogador.invulneravel = False
        Caneta.ativo = False
        # Volta com os sprites normais
        if jogador.cur_sprt == jogador.corrida_blue:
            jogador.trocar_sprite(jogador.corrida)
        else:
            jogador.trocar_sprite(jogador.pulo)

    # Controle do tempo de duração do efeito da Caneca
    # Se passar o tempo
    if janela.time_elapsed() - Cafe.timer >= Cafe.t_efeito and Cafe.ativo:
        # Volta com a velocidade anterior
        Movel.x_vel = Cafe.vel_init
        Cafe.ativo = False

    jogador.controle_morte()
    jogador.corrida.update()
    jogador.corrida_blue.update()

def desenhar_objs(jogador, plataformas, itens):
    for plataforma in plataformas:
        plataforma.draw()

    for item in itens:
        item.draw()

    jogador.controler.draw()
    jogador.cur_sprt.draw()

def criar_objs(plataformas, itens, timer, playing):

    # Testa o intervalo entre a criação dos objetos
    if janela.time_elapsed() - timer >= 1500 and playing:
        aux = randint(0, 5)
        if aux < 2:
            # Cria uma plataforma nova
            plataformas.append(Pontilhada(randint(0, 4), width = randint(Pontilhada.max_width // 5, Pontilhada.max_width // 2)))
        else:
            # Cria uma plataforma nova
            plataformas.append(Plataforma(randint(0, 4), width = randint(Plataforma.max_width // 5, Plataforma.max_width // 2)))
        # Calcula a quantidade de itens na plataforma
        qtd_itens = int(plataformas[-1].width / 88)
        plt = plataformas[-1]

        # Cria os itens em cima da plataforma
        for i in range(qtd_itens):
            aux = randint(0, 100)
            if aux < 1: # 1% de chance de aparecer um café
                itens.append(Cafe(plt.x + 88 * i, plt.y, plt))
            elif aux < 2: # 1% de chance de aparecer uma caneta
                itens.append(Caneta(plt.x + 88 * i, plt.y, plt))
            elif aux < 22 and i == 0: # 20% de chance de aparecer uma borracha (se for borracha, vai ser o único item na plataforma)
                itens.append(Borracha(plt.x + 88 * i, plt.y, plt))
                break
            elif aux < 72: # 70% de chance de aparecer um lápis
                itens.append(Lapis(plt.x + 88 * i, plt.y, plt))
            # 28% de chance de não ter item nenhum

            timer = janela.time_elapsed()

    return timer # Passa o tempo atual para o controle de criação

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
Movel.x_vel = janela.width / 7

itens, plataformas = [], []

# Define objetos do jogo
hud = HUD()
menu = Menu()
Pontilhada.jogador = jogador = Player()
plataformas.append(Plataforma(0, 0))
timer = 0

janela.update()
# Game Loop
# Chama funções das classes para atualizar os objetos
while True:
    fundo.draw()
    # Atualiza o hud (classe HUD)
    hud.atualizar(playing)

    if playing:
        colisoes_objs(jogador, plataformas, itens)
        mover_objs(jogador, plataformas, itens)
        atualizar_objs(jogador, plataformas, itens)
    desenhar_objs(jogador, plataformas, itens)

    # Se pressionar ESC ou o jogo estiver pausado
    if teclado.key_pressed("ESC") or not playing:
        playing = menu.atualizar()

    janela.update()
    # Controle de criação de novos objetos
    timer = criar_objs(plataformas, itens, timer, playing)
