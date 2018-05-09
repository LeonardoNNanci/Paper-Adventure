from PPlay.sprite import *

class HUD():
    # Objetos da main
    janela = None

    # Inicializa classe e objetos e variáveis auxiliares
    def __init__(self):
        # Variáveis contadoras
        self.count_lapis = self.count_dist = 0
        self.icone_lapis = Sprite("../sprites/icone_lapis.png")
        self.icone_dist = Sprite("../sprites/icone_seta.png")
        self.icone_lapis.set_position(125, 10)
        self.icone_dist.set_position(115, HUD.janela.height * 1.15 / 14)

    # Desenha o que é necessario na tela
    def atualizar(self, playing):
        # if playing:
        #   pass
        self.icone_dist.draw()
        self.icone_lapis.draw()
        HUD.janela.draw_text(str(int(self.count_lapis)), 175, -7, size = 45, font_name = "Comic Sans MS", bold = True)
        HUD.janela.draw_text(str(int(self.count_dist)), 175, HUD.janela.height * 0.9 / 14, size = 45, font_name = "Comic Sans MS", bold = True)
