from PPlay.sprite import *

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

    # Controle de movimentação do personagem
    def mover(self, plataformas, itens):
        for item in itens:
            if item.teste_colisao(self):
                itens.remove(item)
                print("ITEM!")
        # Testa colisão com cada plataforma
        for plataforma in plataformas:
            teste_colisao = plataforma.teste_colisao(self)
            if teste_colisao:
                # Se colidir e estiver caindo
                if self.y_vel > 0:
                    # Define corrida como o sprite atual e o posiciona corretamente
                    x, y = self.cur_sprt.x, self.cur_sprt.y
                    self.cur_sprt = self.corrida
                    self.cur_sprt.set_position(x, y)
                    # Anula a velocidade vertical (para de cair)
                    self.y_vel = 0
                    print("Corre") # Print para debug
                # Como a colisão só acontece com uma plataforma por vez, para de testar colisões
                break

        # Se não colidir com nenhuma plataforma
        if teste_colisao == False:
            # Se acabar de perder contato com uma plataforma
            if self.y_vel == 0:
                # Está caindo
                # Define pulo como o sprite atual e o posiciona corretamente
                x, y = self.cur_sprt.x, self.cur_sprt.y
                self.cur_sprt = self.pulo
                self.cur_sprt.set_position(x, y)
                print("Cai") # Print para debug
            # Atualiza velocidade
            # V = Vo + at (Física)
            self.y_vel += self.gravidade * Player.janela.delta_time()

        # Se usuário pressionar Barra de Espaço
        if Player.teclado.key_pressed("SPACE"):
            # Se estiver correndo e pressionar Barra de Espaço
            if teste_colisao and self.y_vel == 0:
                # Atualiza velocidade, funcionando como um "impulso" para cima
                # Quanto mais alto na tela, menor o "impulso"
                self.y_vel = -(Player.janela.height - (self.y_init - self.cur_sprt.y - self.cur_sprt.height))
                # Define pulo como o sprite atual e o posiciona corretamente
                x, y = self.cur_sprt.x, self.cur_sprt.y
                self.cur_sprt = self.pulo
                self.cur_sprt.set_position(x, y)
                print("Pula") # Print para debug
                self.y_saida = y # Ajuda no controle de altura do pulo

            # Se estiver subindo e pressionar Barra de Espaço
            if self.y_vel < 0:
                # Diminui força da gravidade
                # Controle de altura do pulo
                self.gravidade = self.janela.height

            # Se estiver descendo e pressionar Barra de Espaço
            else:
                # Diminui força da gravidade
                # Controle de intensidade da queda
                self.gravidade = Player.janela.height / 5
        # Enquanto não pressionar Barra de Espaço
        else:
            # Se estiver subindo
            if self.y_vel < 0:
                # Gravidade muda de acordo com a posição do inicio do pulo
                self.gravidade = Player.janela.height * 6.4 / (Player.janela.height / self.y_saida)
            # Se estiver descendo
            else:
                self.gravidade = Player.janela.height * 3.2

        # Move o sprite atual e o controlador de colisão
        # de acordo com a velocidade e a aceleração
        # S = So + vt
        self.controler.y += self.y_vel * Player.janela.delta_time()
        self.cur_sprt.y += self.y_vel * Player.janela.delta_time()

    # Controle de game over
    def controle_morte(self):
        # Se sair para baixo da tela
        if self.cur_sprt.y > Player.janela.height:
            # Fecha o jogo
            sys.exit()

    # Chama as funções que atualizam o Stickman
    def atualizar(self, plataformas, itens, playing):
        # Se não estiver pausado
        if playing:
            self.mover(plataformas, itens)
            self.corrida.update()
        self.controle_morte()
        self.cur_sprt.draw()
        # Descomenta o comando de baixo pra ver o controler e entender melhor
        # Se quiser
        # Player.controler.draw()
