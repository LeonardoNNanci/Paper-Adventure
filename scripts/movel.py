from PPlay.sprite import *
from player import *

# Como plataformas e itens têm comportamentos muito semelhantes,
# essa classe reune os comportamentos em comum entre os dois.
# Serve como uma base para as classes Plataforma e Item
class Movel(Sprite):

    # Objeto da main
    janela = None

    # Inicializa a classe
    def __init__(self, img_file):
        Sprite.__init__(self, img_file)

    def colisao(self, obj):
        if obj.x - self.width <= self.x <= obj.x + obj.width:
            if (self.y <= obj.y + obj.height <= self.y + self.height + obj.height):
                return True
        return False

    # Controle de movimentação de iten e plataformas
    def mover(self):
        # Se sair da tela
        if self.x < -self.width:
            # Volta pra extremidade direita
            self.x = Movel.janela.width

        # Movimentação
        # S = So + vt (Física)
        self.x -= 200 * Movel.janela.delta_time()

    # Chama as funções da classe
    def atualizar(self, playing):
        # Se o jogo não estiver pausado
        if playing:
            Movel.mover(self)
        self.draw()

##############################################################################
# Herda as funções da classe Movel
class Item(Movel):
    def __init__(self, tipo, pos_x, pos_y):
        Movel.__init__(self, "../sprites/" + tipo + ".png")
        self.set_position(Movel.janela.width * pos_x / 2, (Movel.janela.height * (13 - pos_y) / 14) - self.height) # Plataforma.janela.width

    # Testa colisao com o "corpo" do jogador
    def teste_colisao(self, jogador):
        return self.colisao(jogador.cur_sprt)

##############################################################################
# Herda as funções da classe Movel
class Plataforma(Movel):
    def __init__(self, pos_x, pos_y):
        Movel.__init__(self, "../sprites/plataforma.jpg")
        self.set_position(Movel.janela.width * pos_x / 2, (Movel.janela.height * (13 - pos_y) / 14)) # Plataforma.janela.width

    # Testa colisão com o controlador de pulos do jogador
    def teste_colisao(self, jogador):
        return self.colisao(jogador.controler)
