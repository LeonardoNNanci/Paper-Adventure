from PPlay.sprite import *

class Player(Sprite):
    janela = True

    def __init__(self, janela):
        Sprite.__init__(self, "../sprites/run-cycle.png", 19)
        Player.janela = janela

    def setup(self):
        self.set_position(110, Player.janela.height * 11 / 14 - 5)
        self.set_total_duration(500)

    def atualizar(self):
        self.draw()
        self.update()
