from PPlay.sprite import *

class Plataforma(Sprite):
    janela = id = True

    def __init__(self, janela):
        # self.id = id
        # if self.id == 0:
        Sprite.__init__(self, "../sprites/plataforma.png")
        # else:
            # Sprite.__init__(self, "../sprites/plataforma_pontilhada.png")
        # self = Sprite.__init__(self, "../sprites/plataforma.png")
        Plataforma.janela = janela

    def setup(self, pos_x, pos_y):
        self.set_position(Plataforma.janela.width * pos_x / 2, Plataforma.janela.height * (13 - pos_y) / 14) # Plataforma.janela.width

    def mover(self):
        if self.x < -self.width:
            self.x = Plataforma.janela.width

        self.x -= 200 * Plataforma.janela.delta_time()


    def atualizar(self, playing):
        if playing:
            Plataforma.mover(self)
        self.draw()
