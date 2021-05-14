from classes.Animal import Animal

class Reptil(Animal):
    def __init__(self, nome, temperaturaCorporal, isReptilTerrestre, qtdePatas):
        super(Reptil, self).__init__(nome)
        self.temperaturaCorporal = temperaturaCorporal
        self.isReptilTerrestre = isReptilTerrestre
        self.qtdePatas = qtdePatas
