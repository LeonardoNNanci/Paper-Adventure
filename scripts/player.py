from PPlay.sprite import *
from PPlay.collision import *
janela = teclado = True

class Player(Sprite):
    cur_sprt = corrida = pulo = controler = janela = teclado = True
    y_vel, gravidade = 0, 2000

    def __init__(self, janela):
        Sprite.__init__(self, "../sprites/empty.png")
        Player.controler = Sprite("../sprites/empty.png")
        Player.corrida = Sprite("../sprites/run-cycle.png", 19)
        Player.pulo = Sprite("../sprites/jump.png")
        Player.janela = janela
        Player.teclado = janela.get_keyboard()

    def setup(self):
        Player.cur_sprt = Player.corrida
        Player.cur_sprt.set_position(110, Player.janela.height * 11 / 14)
        Player.corrida.set_total_duration(500)
        Player.controler.height, Player.controler.width = 10, Player.cur_sprt.width
        Player.controler.set_position(Player.cur_sprt.x, Player.cur_sprt.y + Player.cur_sprt.height-13)


    def mover(self, plataformas):
        for i in range(len(plataformas)):
            teste_colisao = Collision.collided(Player.controler, plataformas[i])
            if teste_colisao and Player.y_vel >= 0:
                x, y = Player.cur_sprt.x, Player.cur_sprt.y
                Player.cur_sprt = Player.corrida
                Player.cur_sprt.set_position(x, y)
                Player.y_vel = 0
                break

        if teste_colisao == False:
            Player.y_vel += Player.gravidade * Player.janela.delta_time()

        if Player.teclado.key_pressed("SPACE"):
            if Player.y_vel == 0:
                Player.y_vel = -(750) * ((Player.cur_sprt.y + Player.cur_sprt.height) / ((13 / 14) * Player.janela.height))
                # ((750) * ((Player.cur_sprt.y + Player.cur_sprt.height) / Player.janela.height)) / 13
                # (Player.cur_sprt.y + Player.cur_sprt.height) / (Player.janela.height * 10 / 14) #((Player.janela.height + 120) * Player.cur_sprt.y) / (Player.janela.height * 10 / 14)
                x, y = Player.cur_sprt.x, Player.cur_sprt.y
                Player.cur_sprt = Player.pulo
                Player.cur_sprt.set_position(x, y)

            if Player.y_vel < 0:
                Player.gravidade = Player.janela.height
            else:
                Player.gravidade = Player.janela.height / 5
        else:
            Player.gravidade = 2000

        Player.controler.y += Player.y_vel * Player.janela.delta_time()
        Player.cur_sprt.y += Player.y_vel * Player.janela.delta_time()

    def atualizar(self, plataformas, itens, playing):
        if playing:
            Player.mover(self, plataformas)
            Player.corrida.update()
        Player.cur_sprt.draw()
