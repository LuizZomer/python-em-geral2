class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self,rua,numero):
        self.enderecos.append(Endereco(rua,numero))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self,rua,numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Centro',56)
cliente1.inserir_endereco('Avenida centenario',90)

cliente1.listar_endereco()