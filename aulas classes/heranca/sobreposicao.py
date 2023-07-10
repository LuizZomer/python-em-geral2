# class MinhaString(str):
#     def upper(self):
#         print('Chamou upper')
#         retorno = super().upper()
#         print('Depois do upper')
#         return retorno


# string = MinhaString('Olá')

# print(string.upper())

class A:
    atributo_a = 'valor 1'

    def __init__(self,atributo):
        self.atributo = atributo 
        
    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor 2'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor 3'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        print('Exquece')

    def metodo(self):
        # super().metodo() Procura no metodo q esta passand oa heranca, no caso o 'B'
        super(B,self).metodo() #Procura no 'A'
        print('C')


c = C('Atribute','qualquer')
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print(c.atributo)
print(c.outra_coisa)
