class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.completo = f'{nome} {sobrenome}'

p1 = Pessoa('Luiz','Zomer')
p2 = Pessoa('Daniel','Freitas')

print(p1.completo)