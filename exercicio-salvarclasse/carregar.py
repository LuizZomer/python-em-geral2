import json
from salvar import caminho, Pessoa

with open(caminho,'r') as arquivo:
    dados = json.load(arquivo)

    p1 = Pessoa(**dados[0])        
    p2 = Pessoa(**dados[1])        
    p3 = Pessoa(**dados[2])        