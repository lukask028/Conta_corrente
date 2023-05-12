# Crie uma classe que modele uma conta corrente
# (a) Atributos: n´umero da conta, nome do correntista e saldo
# (b) M´etodos: alterar nome, dep´ osito e saque; No construtor, saldo ´e opcional, com valor
# default zero e os demais atributos s˜ao obrigat ´ orios.

class contacorrente:
    def __init__(self, numeroconta : int, nome : str, saldo= 0):
        self.numeroconta = numeroconta 
        self.nome = nome 
        self.saldo = saldo 
        
    def saque(self,valor : float):
        valor_pos_saque = self.saldo - valor 
        if valor_pos_saque >= 0:
            self.saldo -= valor
            print('O valor pos saque, na conta é:' f'{self.saldo}')
            return self.saldo
        if valor > self.saldo:
            print("Não foi possível efetuar a ação, saldo indisponível para saque.")
        
    def deposito(self,valor : float):
        valor_pos_deposito = self.saldo + valor 
        if valor_pos_deposito >= 10000:
            print('Não foi possível depositar a quantia, o saldo em conta ultrapassou os 10.000')
            return self.saldo 
        else:
            self.saldo += valor
            print('Seu saldo pos deposito é : 'f'{self.saldo}') 
            return self.saldo
        
    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.numeroconta!r}, {self.nome!r}, {self.saldo!r})'
            return f'{class_name}{attrs}'
        
cliente = contacorrente(123, 'lucas', 5000)
print(cliente)
cliente.saque(8000)
cliente.deposito(100)
cliente.deposito(6100)