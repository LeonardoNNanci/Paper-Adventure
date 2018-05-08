from PPlay.sprite import *

class Player():
    # Objetos (Sprites) auxiliares
    # cur_sprt: sprite Atual | controler: controla colisoes com plataformas
    cur_sprt = corrida = pulo = controler = True
    # Objetos da main
    janela = teclado = True
    # Variáveis de controle na movimentação
    y_vel, gravidade, y_init, y_saida = 0, 2000, 0, 0

    # Inicicializa classe e declara objetos auxiliares
    def __init__(self):
        Player.controler = Sprite("../sprites/empty.jpg")
        Player.corrida = Sprite("../sprites/run-cycle.png", 19)
        Player.pulo = Sprite("../sprites/jump.png")

    # Configurações iniciais
    def setup(self):
        # Define a corrida como sprite inicial
        Player.cur_sprt = Player.corrida

        # Grava e define a posicao inicial do sprite na tela
        Player.y_init = (Player.janela.height * 13 / 14) - Player.cur_sprt.height + 5
        Player.cur_sprt.set_position(110, Player.y_init)

        # Define o tamanho e a posicao iniciais do controlador de colisoes
        Player.controler.height, Player.controler.width = 10, Player.cur_sprt.width
        Player.controler.set_position(Player.cur_sprt.x, Player.cur_sprt.y + Player.cur_sprt.height - 10)

        # Define a duração de um loop da animação de corrida (em milissegundos)
        Player.corrida.set_total_duration(500)

    # Controle de colisao com plataformas
    def colisao_plataforma(plataforma):
        # Se se estiver horizontalmente "longe" do jogador já retorna False
        if plataforma.x <= Player.cur_sprt.x + Player.cur_sprt.width:
            # Se estiver horizontalmente "perto" e tocar na plataforma retorna True
            if (plataforma.y <= Player.controler.y + Player.controler.height <= plataforma.y + plataforma.height + Player.controler.height) and (plataforma.x + plataforma.width >= Player.cur_sprt.x):
                return True
        return False

    # Controle de movimentação do personagem
    def mover(plataformas):
        # Testa colisão com cada plataforma
        for i in range(len(plataformas)):
            teste_colisao = Player.colisao_plataforma(plataformas[i])
            if teste_colisao:
                # Se colidir e estiver caindo
                if Player.y_vel > 0:
                    # Define corrida como o sprite atual e o posiciona corretamente
                    x, y = Player.cur_sprt.x, Player.cur_sprt.y
                    Player.cur_sprt = Player.corrida
                    Player.cur_sprt.set_position(x, y)
                    # Anula a velocidade vertical (para de cair)
                    Player.y_vel = 0
                    print("Corre") # Print para debug
                # Como a colisão só acontece com uma plataforma por vez, para de testar colisões
                break

        # Se não colidir com nenhuma plataforma
        if teste_colisao == False:
            # Se acabar de perder contato com uma plataforma
            if Player.y_vel == 0:
                # Está caindo
                # Define pulo como o sprite atual e o posiciona corretamente
                x, y = Player.cur_sprt.x, Player.cur_sprt.y
                Player.cur_sprt = Player.pulo
                Player.cur_sprt.set_position(x, y)
                print("Cai") # Print para debug
            # Atualiza velocidade
            # V = Vo + at (Física)
            Player.y_vel += Player.gravidade * Player.janela.delta_time()

        # Se usuário pressionar Barra de Espaço
        if Player.teclado.key_pressed("SPACE"):
            # Se estiver correndo e pressionar Barra de Espaço
            if teste_colisao and Player.y_vel == 0:
                # Atualiza velocidade, funcionando como um "impulso" para cima
                # Quanto mais alto na tela, menor o "impulso"
                Player.y_vel = -(Player.janela.height - (Player.y_init - Player.cur_sprt.y - Player.cur_sprt.height))
                # Define pulo como o sprite atual e o posiciona corretamente
                x, y = Player.cur_sprt.x, Player.cur_sprt.y
                Player.cur_sprt = Player.pulo
                Player.cur_sprt.set_position(x, y)
                print("Pula") # Print para debug
                Player.y_saida = y # Ajuda no controle de altura do pulo

            # Se estiver subindo e pressionar Barra de Espaço
            if Player.y_vel < 0:
                # Diminui força da gravidade
                # Controle de altura do pulo
                Player.gravidade = Player.janela.height

            # Se estiver descendo e pressionar Barra de Espaço
            else:
                # Diminui força da gravidade
                # Controle de intensidade da queda
                Player.gravidade = Player.janela.height / 5
        # Enquanto não pressionar Barra de Espaço
        else:
            # Se estiver subindo
            if Player.y_vel < 0:
                # Gravidade muda de acordo com a posição do inicio do pulo
                Player.gravidade = Player.janela.height * 6.4 / (Player.janela.height / Player.y_saida)
            # Se estiver descendo
            else:
                Player.gravidade = Player.janela.height * 3.2

        # Move o sprite atual e o controlador de colisão
        # de acordo com a velocidade e a aceleração
        # S = So + vt
        Player.controler.y += Player.y_vel * Player.janela.delta_time()
        Player.cur_sprt.y += Player.y_vel * Player.janela.delta_time()

    # Controle de game over
    def controle_morte():
        # Se sair para baixo da tela
        if Player.cur_sprt.y > Player.janela.height:
            # Fecha o jogo
            sys.exit()

    # Chama as funções que atualizam o Stickman
    def atualizar(self, plataformas, itens, playing):
        # Se não estiver pausado
        if playing:
            Player.mover(plataformas)
            Player.corrida.update()
        Player.controle_morte()
        Player.cur_sprt.draw()
        # Descomenta o comando de baixo pra ver o controler e entender melhor
        # Se quiser
        # Player.controler.draw()
