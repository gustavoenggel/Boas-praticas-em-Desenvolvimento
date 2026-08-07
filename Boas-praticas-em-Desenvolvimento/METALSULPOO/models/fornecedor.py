class Fornecedor:
    def __init__(self,id, razao_social,cnpj,telefone,email):
        self.__id = id
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.__email = email

    @property
    def id(self):
        return self.__id

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def telefone(self):
        return self.__telefone

    @property
    def email(self):
        return self.__email

    @razao_social.setter
    

    @telefone.setter

    @email.setter
