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
    else:
        try:
            if(isinstance(animalEncontrado[0], Mamifero)):
                print(f'Animal {animalEncontrado[0].nome} encontrao do tipo Mamífero, qtde de Mamas: {animalEncontrado[0].qtdeMamas}')
            elif(isinstance(animalEncontrado[0], Ave)):
                print(f'Animal {animalEncontrado[0].nome} encontrao do tipo Ave, qtde penas: {animalEncontrado[0].qtdePenas}')
            elif(isinstance(animalEncontrado[0], Peixe)):
                print(f'Animal {animalEncontrado[0].nome} encontrao do tipo Peixe, qtde de nadadeiras: {animalEncontrado[0].qtdeNadadeiras}')
            elif(isinstance(animalEncontrado[0], Reptil)):
                print(f'Animal {animalEncontrado[0].nome} encontrao do tipo Reptil, temperatura corporal: {animalEncontrado[0].temperaturaCorporal}')
            else:
                print("Ocorreu um erro ao definir o tipo de animal")
        except Exception as e:
            print("Ocorreu um erro, favor tentar novamente!")