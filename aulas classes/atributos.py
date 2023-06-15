
  
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    
    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Luiz',19)
p2 = Pessoa('Daniel',20)

print(p1.ano_nascimento())
print(p2.ano_nascimento())

# print(p1.__dict__)
print(vars(p1))
