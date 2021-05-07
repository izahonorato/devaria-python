def lavarCarro(posicao):
    print(f'Lavando carro {posicao}')

def VerificarCarroNaFila(posicao):
    if(posicao > 5):
        return False
    else:
        return True

if __name__ == '__main__':
    #estrutura de repetição com intervalo de de valores
    for n in range(0,5):
        print(n)

    #for decrescente
    for n in range(5,0,-1): #inicia em 5 e vai até 0, de um em um
        print(n)

    #for percorrendo caracteres de uma string
    palavra = 'Devaria'
    for letra in palavra:
        print(letra)

    #while crescente
    n = 0
    while n < 5:
        print(n)
        n = n + 1

    temCarroNaFila = True
    posicao = 1
    while(temCarroNaFila):
        lavarCarro(posicao)
        posicao += 1
        temCarroNaFila = VerificarCarroNaFila(posicao)
    else:
        print('Terminou de lavar os carros!')