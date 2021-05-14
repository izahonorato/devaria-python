from Enum.MeioPagamento import MeioPagamento
from classes.Pagamento import Pagamento
from classes.Compra import Compra


if __name__=='__main__':
    produtos_disponiveis = [
        {'nome': 'Chinelo', 'Preço_unidade': 20},
        {'nome': 'Tênis', 'Preço_unidade': 250},
        {'nome': 'Sandália', 'Preço_unidade': 100},
        {'nome': 'Calça', 'Preço_unidade': 120},
    ]
    produtos_selecionados = []
    while True:
        produto_digitado = input('Digite o nome do produto: (sair para sair)')

        if(produto_digitado == 'sair'):
            break

        produtosEncontrados = list(filter(lambda p : p['nome'] == produto_digitado, produtos_disponiveis))

        if len(produtosEncontrados) == 0:
            print('Este produto não foi encontrado, favor, digitar outro')
        else:
            while True:
                try:
                    qtde_produto = int(input(f'Digite a quantidade de {produto_digitado} que você deseja'))
                    break
                except:
                    print('Quantidade digitada incorreta, favor digitar novamente')

            produtos_selecionados.append({
                'nome' : produto_digitado,
                'quantidade' : qtde_produto,
                'valor' : produtosEncontrados[0]['Preço_unidade']
            })

    while True:
        try:
            meio_pagamento_digitado = input('Digite a forma de pagamento: PIX ou Boleto')
            meio_pagamento = MeioPagamento(meio_pagamento_digitado)
            break
        except:
            print('Forma de pagamento inválida, favor digitar novamente')

    compra = Compra(meio_pagamento, produtos_selecionados)
    compra.realizarCompra()


