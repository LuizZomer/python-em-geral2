# Metodo de instancia

# class Connection:
#     def __init__(self,host='localhost'):
#         self.host = host
#         self.user = None
#         self.password = None


#     def set_user(self,user):
#         self.user = user


#     def set_password(self, password):
#         self.password = password


# c1 = Connection()
# c1.set_user('luiz')
# c1.set_password('12345')

# print(c1.user)
# print(c1.password)


# Metodo de classe

class Connection:
    def __init__(self,host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    def set_user(self,user):
        self.user = user


    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls,user,password):
         connection = cls() 
         connection.user = user
         connection.password = password
         return connection



c1 = Connection.create_with_auth('luiz','12345')


