class Console:
    def __init__(self,nome):
        self.nome = nome


    def jogos(self,exclusivo):
        print(f'O {self.nome} tem o jogo {exclusivo} como exclusivo')
    
    
    def lancamento(self,ano):
        print(f'O {self.nome} lançou no ano {ano}') 

ps5 = Console('Ps5')
xbox = Console('Xbox Series X')

ps5.lancamento('2022')
ps5.jogos('God of War:Ragnarok')

xbox.lancamento('2022')
xbox.jogos('Halo 4')