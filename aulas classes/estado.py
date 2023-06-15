class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True


    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto grava')
            return
        
        print(f'{self.nome} tirou a foto')
    

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
        
        print(f'{self.nome} está parando de filmar')
        self.filmando = False


c1 = Camera('Canon')
c2 = Camera('Sony')


print(c1.D)
print(c2.filmando)
c1.fotografar()