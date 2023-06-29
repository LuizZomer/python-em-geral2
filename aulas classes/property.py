class Caneta:
    def __init__(self, cor):
        self.cor = cor


    @property
    def cor_tinta(self):
        print('Property')
        return self.cor

    # get em outras linguagens

    # def get_cor(self):
    #     return self.cor_tinta

caneta = Caneta('azul')

print(caneta.cor_tinta)

