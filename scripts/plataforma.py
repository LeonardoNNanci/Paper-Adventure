from PPlay.sprite import *

class Plataforma(Sprite):
    janela = id = True

    def __init__(self, janela, id):
        self.id = id
        if self.id == 0:
            Sprite.__init__(self, "../sprites/plataforma.png")
        else:
            Sprite.__init__(self, "../sprites/plataforma_pontilhada.png")
        # self = Sprite.__init__(self, "../sprites/plataforma.png")
        Plataforma.janela = janela

    def setup(self, pos_x, pos_y):
        self.set_position(Plataforma.janela.width * pos_x / 20, Plataforma.janela.height * pos_y / 14)

    def atualizar(self):
        self.draw()
