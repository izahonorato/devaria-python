from classes.Animal import Animal

class Peixe(Animal):
    def __init__(self, nome, qtdeNadadeiras, isPeixeAguaSalgada, isCarnivoro):
        super(Peixe, self).__init__(nome)
        self.qtdeNadadeiras = qtdeNadadeiras
        self.isPeixeAguaSalgada = isPeixeAguaSalgada
        self.isCarnivoro = isCarnivoro
