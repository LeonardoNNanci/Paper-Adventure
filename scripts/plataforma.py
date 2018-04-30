from PPlay.sprite import *

class Plataforma(Sprite):
    janela = True

    def __init__(self, janela):
        self = Sprite.__init__(self, "../sprites/plataforma.png")
        # self = Sprite.__init__(self, "../sprites/plataforma.png")
        Plataforma.janela = janela

    def setup(self):
        self.set_position(0, Plataforma.janela.height * 13 / 14)

    def atualizar(self):
        self.draw()
