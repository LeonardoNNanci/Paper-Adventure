from PPlay.sprite import *

class Item(Sprite):

    # Objeto da main
    janela = True

    # Inicializa a classe
    def __init__(self, img_file):
        Sprite.__init__(self, img_file)

    # Configurações iniciais
    def setup(self, pos_x, pos_y):
        self.set_position(Item.janela.width * pos_x / 2, Item.janela.height * (13 - pos_y) / 14) # Plataforma.janela.width

    # Controle de movimentação de cada item
    def mover(self):
        # Se sair da tela
        if self.x < -self.width:
            # Volta pra extremidade direita
            self.x = Item.janela.width

        # Movimentação
        # S = So + vt (Física)
        self.x -= 200 * Item.janela.delta_time()

    # Chama as funções da classe
    def atualizar(self, playing):
        # Se o jogo não estiver pausado
        if playing:
            Item.mover(self)
        self.draw()
