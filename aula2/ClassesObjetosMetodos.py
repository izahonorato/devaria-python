class ContaBancaria:
    def __init__(self, tipo, conta, agencia): #criando a classe
        self.tipo = tipo
        self.conta = conta
        self.agencia = agencia

    def exibirDadosConta(self): #criando o método da classe
        print('Informações da conta: ')
        print(f'Conta criada, tipo: {self.tipo} - conta: {self.conta} - agencia: {self.agencia}')


if __name__ == '__main__':
    conta1 = ContaBancaria('corrente', 6548, '57002') #instanciando o objeto
    conta1.exibirDadosConta()

    conta1.tipo = 'poupança' #alterando o tipo de um obj ja criado
    conta1.exibirDadosConta()

    conta2 = ContaBancaria('poupança', 3333, '57745')  # instanciando o objeto
    conta2.exibirDadosConta()