from PPlay.sprite import *

class Item(Sprite):
    janela = True
    id = 0

    # id identifica cada item |lapis = 0|caneta = 1|borracha = 2|cafe = 3|
    def __init__(self, id, janela):
        Item.janela = janela
        self.id = id
        if(id == 0):
            Sprite.__init__(self, "../sprites/lapis.png")
        elif(id == 1):
            Sprite.__init__(self, "../sprites/caneta.png")
        elif(id == 2):
            Sprite.__init__(self, "../sprites/borracha.png")
        elif(id == 3):
            Sprite.__init__(self, "../sprites/cafe.png")


    def setup(self):
        if(self.id == 0):
            self.set_position(250, Item.janela.height * 11.75 / 14)
        elif(self.id == 1):
            self.set_position(310, Item.janela.height * 11.5 / 14)
        elif(self.id == 2):
            self.set_position(370, Item.janela.height * 11.5 / 14)
        elif(self.id == 3):
            self.set_position(475, Item.janela.height * 11.6 / 14)

    def atualizar(self):
        self.draw()
