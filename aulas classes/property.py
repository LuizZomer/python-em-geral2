class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor_tinta(self):
        print('Property')
        return self._cor

    @cor_tinta.setter
    def cor(self,valor):
        self._cor = valor

    # get em outras linguagens

    # def get_cor(self):
    #     return self.cor_tinta

caneta = Caneta('azul')

print(caneta.cor_tinta)
caneta.cor = 'rosa'

print(caneta.cor)