#Object
class Pessoa(object):
    def __init__(self,nome,sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome
    

    def falar(self):
        print(self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...

c1 = Cliente('Luiz','Zomer')
c2 = Aluno('Daniel','Silva')

c1.falar()
c2.falar()