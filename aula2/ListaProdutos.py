if __name__ == '__main__':
    produtos = []
    produtosMercado = ['Refrigerante', 'Cerveja', 'Maçã', 'Arroz', 'Carne']

    while True:
        produto = input("Digite um produto para adicionar na lista (Digite sair para encerrar): ")

        if produto == 'sair':
            break
        produtos.append(produto)

    produtosIndisponiveis = []
    produtosDisponiveis = []

    for p in produtos:
        if not p in produtosMercado:
            produtosIndisponiveis.append(p)
        else:
            produtosDisponiveis.append(p)

    print(f'Estes produtos nós temos: {produtosDisponiveis}')
    print(f'Estes produtos nós não temos: {produtosIndisponiveis}')

    produtosMercado.sort()
    print(f'Produtos disponíveis em ordem alfabética: {produtosMercado}')
