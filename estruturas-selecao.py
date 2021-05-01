if __name__ == '__estruturas-selecao__':
    nota = int(input('Digite uma nota: '))

    if nota <= 30:
        print('Você foi reprovada!')
    elif nota <= 60:
        print('Ficou de rec!')
    else:
        print('Parabéns, você está aprovada!')

def SecondOperand():
    print("Testando a segunda condição")
    return True

if __name__ == '__main__':
    a = False and SecondOperand()
    print(a)
    b = True and SecondOperand()
    print(b)