import json

caminho = 'banco.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Luiz',19)
p2 = Pessoa('Daniel',20)
p3 = Pessoa('Arthur',18)
bd = [vars(p1),vars(p2),vars(p3)]

if __name__ == '__main__':
    with open(caminho,'w') as arquivo:
        json.dump(bd,arquivo,ensure_ascii=False,indent=2)