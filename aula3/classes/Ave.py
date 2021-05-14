from classes.Animal import Animal

class Ave(Animal):
    def __init__(self, nome, qtdePenas, consegueVoar, consegueFazerMigracao):
        super().__init__(nome)
        self.qtdePenas = qtdePenas
        self.consegueVoar = consegueVoar
        self.consegueFazerMigracao = consegueFazerMigracao
        