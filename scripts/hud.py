from PPlay.sprite import *

class HUD(Sprite):
    janela = True
    lapis = dist = 0

    def __init__(self, janela):
        Sprite.__init__(self, "../sprites/empty.png")
        HUD.janela = janela


    def setup(self):
        HUD.icone_lapis = Sprite("../sprites/icone_lapis.png")
        HUD.icone_lapis.set_position(125, 10)
        HUD.icone_dist = Sprite("../sprites/icone_seta.png")
        HUD.icone_dist.set_position(115, HUD.janela.height * 1.15 / 14)

    def atualizar(self):
        HUD.icone_dist.draw()
        HUD.icone_lapis.draw()
        HUD.janela.draw_text(str(HUD.lapis), 175, -7, size = 45, font_name = "Comic Sans MS", bold = True)
        HUD.janela.draw_text(str(HUD.dist), 175, HUD.janela.height * 0.9 / 14, size = 45, font_name = "Comic Sans MS", bold = True)
