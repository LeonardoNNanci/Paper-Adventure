from PPlay.sprite import *
from itens import *

class Player():
    # Objetos da main
    janela = teclado = None

    # Inicicializa classe e declara objetos auxiliares
    def __init__(self):
        # Variáveis de controle na movimentação
        self.y_vel, self.gravidade, self.y_saida = 0, 2000, 0

        # Objetos (Sprites) auxiliares
        # cur_sprt: sprite Atual | controler: controla colisoes com plataformas
        self.controler = Sprite("../sprites/empty.jpg")
        self.corrida = Sprite("../sprites/run-cycle.png", 19)
        self.pulo = Sprite("../sprites/jump.png")
        self.corrida_blue = Sprite("../sprites/run-cycle_blue.png", 19)
        self.pulo_blue = Sprite("../sprites/jump_blue.png")

        # Define a corrida como sprite inicial
        self.cur_sprt = self.corrida

        # Grava e define a posicao inicial do sprite na tela
        self.y_init = (Player.janela.height * 13 / 14) - self.cur_sprt.height + 5
        self.cur_sprt.set_position(110, self.y_init)

        # Define o tamanho e a posicao iniciais do controlador de colisoes
        self.controler.height, self.controler.width = 10, self.cur_sprt.width
        self.controler.set_position(self.cur_sprt.x, self.cur_sprt.y + self.cur_sprt.height - 10)

        # Define a duração de um loop da animação de corrida (em milissegundos)
        self.corrida.set_total_duration(500)
        self.corrida_blue.set_total_duration(500)

        # Variaveis auxiliares
        self.colisao = False
        self.invulneravel = False

    def mover(self, plataformas, itens):
        # Testa se a Barra de Espaco foi pressionada
        espaco = Player.teclado.key_pressed("SPACE")

        if self.colisao:
            # Algoritmo de pulo
            if espaco and self.y_vel >= 0:
                # Atualiza velocidade, funcionando como um "impulso" para cima
                # Quanto mais alto na tela, menor o "impulso"
                self.y_vel = -(Player.janela.height - (self.y_init - self.cur_sprt.y - self.cur_sprt.height))
                self.y_saida = self.cur_sprt.y # Ajuda no controle de altura do pulo
                # Define pulo como o sprite atual
                if self.invulneravel:
                    self.trocar_sprite(self.pulo_blue)
                else:
                    self.trocar_sprite(self.pulo)

            # Algoritmo para corrida
            elif not espaco and self.y_vel > 0:
                # Define corrida como o sprite atual
                if self.invulneravel:
                    self.trocar_sprite(self.corrida_blue)
                else:
                    self.trocar_sprite(self.corrida)
                # Anula a velocidade vertical (para de cair)
                self.y_vel = 0
        else:
            if espaco:
                if self.y_vel < 0:
                    # Diminui força da gravidade
                    # Controle de altura do pulo
                    self.gravidade = self.janela.height
                else:
                    # Diminui força da gravidade
                    # Controle de intensidade da queda
                    self.gravidade = Player.janela.height / 5
            else:
                # Cai
                if self.y_vel == 0:
                    pass
                    # Define pulo como o sprite atual
                    if self.invulneravel:
                        self.trocar_sprite(self.pulo_blue)
                    elif Player.janela.time_elapsed() > 0:
                        self.trocar_sprite(self.pulo)
                elif self.y_vel > 0:
                    # Gravidade 'padrão'
                    self.gravidade = Player.janela.height * 3.2
                else:
                    # Gravidade muda de acordo com a posição do inicio do pulo
                    self.gravidade = Player.janela.height * 6.4 / (Player.janela.height / self.y_saida)

            # Atualiza velocidade e posicao do player
            self.y_vel += self.gravidade * Player.janela.delta_time()
        self.controler.y += self.y_vel * Player.janela.delta_time()
        self.cur_sprt.y += self.y_vel * Player.janela.delta_time()

    # Controle de game over
    def controle_morte(self):
        # Se sair para baixo da tela
        if self.cur_sprt.y > Player.janela.height:
            # Fecha o jogo
            print("Morte por: Queda")
            sys.exit()

    def trocar_sprite(self, sprt):
        # Define o sprite atual e o posiciona corretamente
        x, y = self.cur_sprt.x, self.cur_sprt.y
        self.cur_sprt = sprt
        self.cur_sprt.set_position(x, y)

    def controle_efeitos(self):
        # Controle do tempo de duração do efeito da Caneta
        # Se passar o tempo
        if Player.janela.time_elapsed() - Caneta.timer >= 10000 and Caneta.ativo:
            self.invulneravel = False
            Caneta.ativo = False
            # Volta com os sprites normais
            if self.colisao and self.y_vel == 0:
                self.trocar_sprite(self.corrida)
            else:
                self.trocar_sprite(self.pulo)

        # Controle do tempo de duração do efeito da Caneca
        # Se passar o tempo
        if Player.janela.time_elapsed() - Cafe.timer >= 10000 and Cafe.ativo:
            # Volta com a velocidade anterior
            Movel.x_vel = Cafe.vel_init
            Cafe.ativo = False

    # Chama as funções que atualizam o Stickman
    def atualizar(self, plataformas, itens, playing):
        # Se não estiver pausado
        if playing:
            self.mover(plataformas, itens)
            self.controle_morte()
            self.controle_efeitos()
            self.corrida.update()
            self.corrida_blue.update()
        self.cur_sprt.draw()
        # Descomenta o comando de baixo pra ver o controler e entender melhor
        # Se quiser
        # Player.controler.draw()
