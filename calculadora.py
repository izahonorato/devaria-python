def soma(n1, n2):
    print(f' A soma de {n1} e {n2} é igual a:')
    resultado = n1 + n2
    return resultado

def sub(n1, n2):
    print(f' A subtração de {n1} e {n2} é igual a:')
    resultado = n1 - n2
    return resultado

def mult(n1, n2):
    print(f' A multiplicação de {n1} e {n2} é igual a:')
    resultado = n1 * n2
    return resultado

def div(n1, n2):
    print(f' A divisão de {n1} e {n2} é igual a:')
    resultado = n1 / n2
    return resultado

def mod(n1, n2):
    print(f' O módulo de {n1} e {n2} é igual a:')
    resultado = n1 % n2
    return resultado


if __name__ == '__main__':

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    operador = input('Qual operação você quer fazer? [+, -, *, /, %]: ')

    if operador == '+':
        resultado = soma(num1, num2)
        print(f'{resultado} ')
    elif operador == '-':
        resultado = sub(num1,num2)
        print(f'{resultado} ')
    elif operador == '*':
        resultado = mult(num1, num2)
        print(f'{resultado} ')
    elif operador == '/':
        resultado = div(num1, num2)
        print(f'{resultado} ')
    elif operador == '%':
        resultado = mod(num1, num2)
        print(f'{resultado} ')
    else:
        print('Operador inválido!')
