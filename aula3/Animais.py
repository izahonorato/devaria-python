from classes.Mamifero import Mamifero
from classes.Reptil import Reptil
from classes.Ave import Ave
from classes.Peixe import Peixe
from classes.Animal import Animal

if __name__ == '__main__':

    listaAnimais = [
        Mamifero('Leão', 4, False, False),
        Reptil('Serpente', 25, True, 0),
        Ave('Gavião', 500, True, False),
        Peixe('Turabão', 2, True, True)
    ]

    nomeAnimal = input("Digite o nome do animal: ")

    animalEncontrado = list(filter(lambda animal : animal.nome == nomeAnimal, listaAnimais))

    if len(animalEncontrado) == 0:
        print('Animal não encontrado')
    else: print(animalEncontrado[0].nome)