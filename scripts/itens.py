from PPlay.sprite import *
from PPlay.collision import *
from movel import *
from hud import *

class Cafe(Item):
    vel_init = timer = 0
    ativo = False
    def __init__(self, x, y):
        Item.__init__(self, "../sprites/cafe.png", x, y)

    def efeito(self, jogador):
        # Se já não houver um café ativo
        if not Cafe.ativo:
            # Salva a velocidade anterior ao efeito
            Cafe.vel_init = Movel.x_vel
            # Dobra a velocidade do jogo
            Movel.x_vel *= 2
            # Indica que já há um café ativo
            Cafe.ativo = True
        # Ajuda na indicação do tempo em que fica ativo
        Cafe.timer = Movel.janela.time_elapsed()

class Lapis(Item):
    def __init__(self, x, y):
        Item.__init__(self, "../sprites/lapis.png", x, y)

    def efeito(self, jogador):
        HUD.count_lapis += 1

class Caneta(Item):
    timer = 0
    ativo = False

    def __init__(self, x, y):
        Item.__init__(self, "../sprites/caneta.png", x, y)

    def efeito(self, jogador):
        # Se não houver uma caneta ativa
        if not Caneta.ativo:
            # O Jogador fica invulnerável
            jogador.invulneravel = True
            # Indica que há uma caneta ativa
            Caneta.ativo = True
            # Troca o Sprite para o de caneta
            jogador.trocar_sprite(jogador.corrida_blue)
        # Ajuda na indicação do tempo em que fica ativo
        Caneta.timer = Movel.janela.time_elapsed()

class Borracha(Item):

    def __init__(self, x, y, plataforma):
        Item.__init__(self, "../sprites/borracha.png", x, y)
        self.plataforma = plataforma
        self.ativo = True

    def efeito(self, jogador):
        if not jogador.invulneravel and self.ativo:
            # Se não tiver lápis sufucientes
            if HUD.count_lapis < 10:
                print("Morte por: Borracha")
                sys.exit()
            else:
                HUD.count_lapis -= 10
                self.ativo = False

    def mover(self):
        # Se estiver na extremidade esquerda
        if self.x < self.plataforma.x:
            # Anda para a direita
            self.x_vel = -Movel.janela.width / 5
        # Se estiver na extremidade direita
        elif self.x + self.width > self.plataforma.x + self.plataforma.width:
            # Anda para a esquerda
            self.x_vel = Movel.janela.width / 5


        self.x -= (Movel.x_vel + self.x_vel) * Movel.janela.delta_time()

    # Substitui a função da classe Movel
    def colisao(self, obj):
        # Se estiver na direção do jogador em X
        if obj.x - self.width <= self.x <= obj.x + obj.width:
            return Collision.collided_perfect(self, obj)
        else:
            return False

class Pontilhada(Item):
    pass
