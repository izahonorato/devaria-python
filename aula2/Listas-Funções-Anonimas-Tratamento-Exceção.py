if __name__ == '__main__':

    #tratamento de exceção com try except
    try:
        pessoas = []
        while True:
            nome = input("Digite um nome para adicionar na lista e digite sair para parar: ")

            if nome == 'sair':
                break

            pessoas.append(nome)

        print("Pessoas na lista: ")
        print(pessoas)

        pessoas.sort() #.sort(reverse=True) vai voltar em ordem alfabética ao contrario

        print(pessoas)

        #insere objetos em uma posição especifica, empurrando os outros pra frente
        pessoas.insert(2, "Sara")
        print(pessoas)

        print(f'Quantidade de Ana na lista {pessoas.count("Ana")}')

        notasAlunos = [50, 60, 35, 97, 77]
        mediaNotas = lambda notas: sum(notas) / len(notas) #função anônima ou lambda

        print(f'A media das notas dos alunos é : {mediaNotas(notasAlunos)}')

        notasFiltradas = list(filter(lambda nota : nota > 80, notasAlunos))
        print(f'Notas filtradas acima de 80: {notasFiltradas}')

    except Exception as e:
        print("Erro")