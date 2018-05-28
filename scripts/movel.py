from PPlay.sprite import *

# Como plataformas e itens têm comportamentos muito semelhantes,
# essa classe reune os comportamentos em comum entre os dois.
# Serve como uma base para as classes Plataforma e Item
class Movel(Sprite):

    # Objeto da main
    janela = None

    # Variavel de velocidade
    x_vel = 0

    # Inicializa a classe
    def __init__(self, img_file):
        Sprite.__init__(self, img_file)

    # Controle de colisão
    def colisao(self, obj):
        if obj.x - self.width <= self.x <= obj.x + obj.width:
            if (self.y <= obj.y + obj.height <= self.y + self.height + obj.height):
                return True
        else:
            return False

    # Controle de movimentação de iten e plataformas
    def mover(self):
        # Movimentação
        # S = So + vt (Física)
        self.x -= Movel.x_vel * Movel.janela.delta_time()

# Herda as funções da classe Movel
class Item(Movel):

    def __init__(self, img_file, x, y):
        Movel.__init__(self, img_file)
        self.set_position(x, y - self.height) # Plataforma.janela.width

    # Chama as funções da classe
    def atualizar(self, jogador, playing):
        # Se o jogo não estiver pausado
        if playing:
            self.mover()
        self.draw()
        return self.colisao(jogador.cur_sprt)

# Herda as funções da classe Movel
class Plataforma(Movel):
    max_width = 1280

    def __init__(self, pos_y, pos_x = max_width, width = max_width):
        Movel.__init__(self, "../sprites/plataforma.jpg")
        self.set_position(pos_x, (Movel.janela.height * (13 - pos_y * 2) / 14)) # Plataforma.janela.width
        self.width = width

    # Chama as funções da classe
    def atualizar(self, jogador, playing):
        # Se o jogo não estiver pausado
        if playing:
            Movel.mover(self)
        if self.colisao(jogador.controler) and jogador.colisao == False:
            jogador.colisao = True
        self.draw()
