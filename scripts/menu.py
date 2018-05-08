from PPlay.sprite import *

class Menu():
    # Objetos da main
    janela = mouse = True
    # Objetos auxiliares
    alpha = papel = True
    # Lista de botões
    botoes = []
    # Variavel auxiliar
    hover_b4 = False

    # Inicializa objetos auxiliares
    def __init__(self):
        Menu.alpha = Sprite("../sprites/alpha.png")
        Menu.papel = Sprite("../sprites/post-it.png")
        Menu.botoes.append(Sprite("../sprites/resume.png")) # Adiciona os botoes à lista
        Menu.botoes.append(Sprite("../sprites/sair.png")) # Adiciona os botoes à lista
        Menu.papel.set_position((Menu.janela.width - Menu.papel.width) / 2, (Menu.janela.height - Menu.papel.height) / 2)
        Menu.botoes[0].set_position((Menu.janela.width - Menu.botoes[0].width) / 2 - 20, (Menu.janela.height - Menu.botoes[0].height) / 3)
        Menu.botoes[1].set_position((Menu.janela.width - Menu.botoes[1].width) / 2, (Menu.janela.height - Menu.botoes[1].height) * 2 / 3)

    # Controle de ações dos botões
    # Tem que melhorar isso.
    # Tá atualizando o sprite em todos os frames sem exceção
    # Tô com preguica agora :D
    def controle_click():
        # Se o cursor estiver sobre o botão "Resume"
        if Menu.mouse.is_over_object(Menu.botoes[0]):
            if not Menu.hover_b4:
                # Define o sprite e o posiciona
                Menu.botoes[0] = Sprite("../sprites/resume_hover.png")
                Menu.botoes[0].set_position((Menu.janela.width - Menu.botoes[0].width) / 2 - 20, (Menu.janela.height - Menu.botoes[0].height) / 3)
                Menu.hover_b4 = True
                print(Menu.hover_b4)
            # Se clicar no botão:
            if Menu.mouse.is_button_pressed(1):
                return True

        # Se o cursor estiver sobre o botão "Sair"
        elif Menu.mouse.is_over_object(Menu.botoes[1]):
            if not Menu.hover_b4:
                # Define o sprite e o posiciona
                Menu.botoes[1] = Sprite("../sprites/sair_hover.png")
                Menu.botoes[1].set_position((Menu.janela.width - Menu.botoes[1].width) / 2, (Menu.janela.height - Menu.botoes[1].height) * 2 / 3)
                Menu.hover_b4 = True
                print(Menu.hover_b4)
            # Se clicar no botão:
            if Menu.mouse.is_button_pressed(1):
                sys.exit() # Fecha o jogo
        # Se não estiver sobre nenhum botão
        else:
            if Menu.hover_b4:
                # Define o sprite e o posiciona
                Menu.botoes[0] = Sprite("../sprites/resume.png")
                Menu.botoes[1] = Sprite("../sprites/sair.png")
                Menu.botoes[0].set_position((Menu.janela.width - Menu.botoes[0].width) / 2 - 20, (Menu.janela.height - Menu.botoes[0].height) / 3)
                Menu.botoes[1].set_position((Menu.janela.width - Menu.botoes[1].width) / 2, (Menu.janela.height - Menu.botoes[1].height) * 2 / 3)
                Menu.hover_b4 = False
                print(Menu.hover_b4)
        # Retorno padrão (sem clicar em nenhum botao)
        return False


    # Chama as funções da classe e desenha o que for necessário
    def atualizar():
        # Menu.alpha.draw()
        Menu.papel.draw()
        for i in range(len(Menu.botoes)): # Desenha cada botão
            Menu.botoes[i].draw()
        return Menu.controle_click()
