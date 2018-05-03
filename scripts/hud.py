from PPlay.sprite import *

class HUD():
    # Objetos da main
    janela = True
    # Variáveis contadoras
    count_lapis = count_dist = 0

    # Inicializa classe e declara objetos auxiliares
    def __init__(self):
        HUD.icone_lapis = Sprite("../sprites/icone_lapis.png")
        HUD.icone_dist = Sprite("../sprites/icone_seta.png")

    # Configurações iniciais
    def setup(self):
        HUD.icone_lapis.set_position(125, 10)
        HUD.icone_dist.set_position(115, HUD.janela.height * 1.15 / 14)

    # Desenha o que é necessario na tela
    def atualizar(self, playing):
        # if playing:
        #     HUD.count_dist = 1/(HUD.janela.delta_time() + 0.0000001)
        HUD.icone_dist.draw()
        HUD.icone_lapis.draw()
        HUD.janela.draw_text(str(HUD.count_lapis), 175, -7, size = 45, font_name = "Comic Sans MS", bold = True)
        HUD.janela.draw_text(str(HUD.count_dist), 175, HUD.janela.height * 0.9 / 14, size = 45, font_name = "Comic Sans MS", bold = True)
