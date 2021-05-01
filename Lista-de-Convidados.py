if __name__ == '__Lista-de-Convidados__':
    listaConvidados = ['Izaura', 'Amanda', 'Rafael']

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    estaNaLista = nome in listaConvidados

    maioridade = idade >= 18

    if estaNaLista: #poderia ser if nome in listaConvidados, nesse caso nao precisaria da variavel estaNaLista
        if maioridade:
            print('Bem-vinda à festa!')
        else:
            print('Desculpe, seu nome está na lista mas você é menor de idade...')
    else:
        print('Desculpe você não está na lista')