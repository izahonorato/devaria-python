from classes.Animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, qtdeMamas, isMamiferoAquatico, consegueBotarOvo):
        super().__init__(nome)
        self.qtdeMamas  = qtdeMamas
        self.isMamiferoAquatico = isMamiferoAquatico
        self.consegueBotarOvo = consegueBotarOvo